from django.contrib import admin
from django_tenants.utils import get_tenant_model, get_tenant_domain_model
from django.db import connection
from django.core.exceptions import PermissionDenied

Client = get_tenant_model()
Domain = get_tenant_domain_model()

class PublicSchemaOnlyAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
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
        if connection.schema_name != 'public':
            raise PermissionDenied("Access to this model is restricted to the public schema")
        return super().get_queryset(request)

@admin.register(Client)
class ClientAdmin(PublicSchemaOnlyAdmin):
    list_display = ['name', 'schema_name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'schema_name']

@admin.register(Domain)
class DomainAdmin(PublicSchemaOnlyAdmin):
    list_display = ['domain', 'tenant', 'is_primary']
    list_filter = ['is_primary']
    search_fields = ['domain']