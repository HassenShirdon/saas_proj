from django.contrib import admin
from django_tenants.utils import get_tenant_model, get_tenant_domain_model
from django.db import connection
from django.core.exceptions import PermissionDenied

# Get tenant and domain models
Client = get_tenant_model()
Domain = get_tenant_domain_model()

class PublicSchemaOnlyAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        # Only allow access in public schema for superusers
        return connection.schema_name == 'public' and request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return self.has_module_permission(request)

    def has_add_permission(self, request):
        return self.has_module_permission(request)

    def has_change_permission(self, request, obj=None):
        return self.has_module_permission(request)

    def has_delete_permission(self, request, obj=None):
        return self.has_module_permission(request)

    def get_queryset(self, request):
        # Ensure queryset is only accessible in public schema
        if connection.schema_name != 'public':
            raise PermissionDenied("Access to this model is restricted to the public schema")
        return super().get_queryset(request)

# Register models with restricted admin class
admin.site.register(Client, PublicSchemaOnlyAdmin)
admin.site.register(Domain, PublicSchemaOnlyAdmin)