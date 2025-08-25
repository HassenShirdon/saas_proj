# core/backends.py (NEW FILE)
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db import connection

class TenantAwareAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        
        try:
            # First try to find user in public schema (superusers)
            with connection.cursor() as cursor:
                cursor.execute("SET search_path TO public")
            
            user = UserModel._default_manager.get_by_natural_key(username)
            
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
                
        except UserModel.DoesNotExist:
            # Try to find user in tenant schemas
            from .models import Tenant
            tenants = Tenant.objects.all()
            
            for tenant in tenants:
                try:
                    connection.set_schema(tenant.schema_name)
                    user = UserModel._default_manager.get_by_natural_key(username)
                    
                    if user.check_password(password) and self.user_can_authenticate(user):
                        return user
                        
                except UserModel.DoesNotExist:
                    continue
                finally:
                    # Reset to public schema
                    connection.set_schema_to_public()
                    
        return None