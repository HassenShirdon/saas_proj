from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Tenant, Domain

@admin.register(Tenant)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('tenant_name', 'schema_name', 'is_active')
        list_filter = ('is_active', 'created_on')
        search_fields = ('tenant_name','schema_name')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    list_filter = ('is_primary',)
    search_fields = ('domain','tenant__name')