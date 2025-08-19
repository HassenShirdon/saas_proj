from django.http import JsonResponse
from django_tenants.utils import get_tenant_model, get_public_schema_name
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.conf import settings

class TenantAuthValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip validation for authentication endpoints (your views already handle this)
        if request.path in ['/api/auth/login/', '/admin/login/', '/admin/logout/']:
            return self.get_response(request)
        
        # Skip for non-API routes and static files
        if not request.path.startswith('/api/') or request.path.startswith(settings.STATIC_URL):
            return self.get_response(request)
        
        # Use the same tenant detection logic as your views
        try:
            TenantModel = get_tenant_model()
            hostname = request.get_host().split(':')[0]
            
            if hostname in ['localhost', '127.0.0.1']:
                current_tenant = TenantModel.objects.get(schema_name=get_public_schema_name())
            else:
                subdomain = hostname.split('.')[0]
                current_tenant = TenantModel.objects.get(schema_name=subdomain)
        except:
            # If tenant detection fails, let other middleware handle it
            return self.get_response(request)
        
        # Authenticate the user from JWT token
        jwt_auth = JWTAuthentication()
        try:
            auth_result = jwt_auth.authenticate(request)
            if auth_result:
                user, token = auth_result
                
                # Validate user belongs to current tenant (CRITICAL SECURITY CHECK)
                if user.tenant != current_tenant:
                    return JsonResponse(
                        {
                            'detail': 'Access denied: User not authorized for this tenant schema',
                            'user_tenant': str(user.tenant.schema_name) if user.tenant else 'None',
                            'current_tenant': str(current_tenant.schema_name)
                        },
                        status=status.HTTP_403_FORBIDDEN
                    )
        except Exception as e:
            # If authentication fails, continue (other middleware will handle auth)
            pass
        
        return self.get_response(request)