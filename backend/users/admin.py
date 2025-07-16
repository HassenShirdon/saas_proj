from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_tenant_admin', 'is_active']
    list_filter = ['is_tenant_admin', 'is_active']
    search_fields = ['username', 'email']
    fieldsets = UserAdmin.fieldsets + (
        ('Tenant Settings', {'fields': ('is_tenant_admin',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Tenant Settings', {'fields': ('is_tenant_admin',)}),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_tenant_admin:
            return qs.filter(created_by__tenant_admin=True)
        return qs

    def has_add_permission(self, request):
        return request.user.tenant_admin or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.tenant_admin or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.tenant_admin or request.user.is_superuser

admin.site.register(CustomUser, CustomUserAdmin)