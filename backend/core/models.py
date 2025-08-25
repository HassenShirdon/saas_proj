# core/models.py
from django_tenants.models import TenantMixin, DomainMixin
from django.db import models
from django_tenants.utils import get_public_schema_name

class Tenant(TenantMixin):
    tenant_name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    created_on = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    max_users = models.IntegerField(default=10)  # Increased default
    
    auto_create_schema = True
    auto_drop_schema = True
    
    class Meta:
        db_table = 'core_tenant'  # Explicit table name
    
    def __str__(self):
        return self.tenant_name
    
    def is_public(self):
        return self.schema_name == get_public_schema_name()
    
    def get_user_count(self):
        """Get number of users in this tenant"""
        from django_tenants.utils import tenant_context
        from users.models import User
        
        with tenant_context(self):
            return User.objects.count()

class Domain(DomainMixin):
    is_primary = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'core_domain'  # Explicit table name
    
    def __str__(self):
        return self.domain