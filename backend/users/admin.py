from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_tenants.utils import get_public_schema_name
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Fields to display in list view
    list_display = ('email', 'first_name', 'last_name', 'tenant', 'is_active', 'is_staff')
    list_filter = ('tenant', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    # Fields for editing users
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'avatar')}),
        ('Tenant Info', {'fields': ('tenant',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields for creating users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'tenant', 'is_staff', 'is_active')}
        ),
    )
    
    def get_queryset(self, request):
        # Superusers see all users, staff see only their tenant's users
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(tenant=request.user.tenant)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Limit tenant choices for non-superusers
        if not request.user.is_superuser:
            if 'tenant' in form.base_fields:
                form.base_fields['tenant'].queryset = form.base_fields['tenant'].queryset.filter(
                    id=request.user.tenant.id
                )
                form.base_fields['tenant'].empty_label = None
        
        return form
    
    def save_model(self, request, obj, form, change):
        # Auto-assign tenant for non-superusers if not set
        if not obj.is_superuser and not obj.tenant:
            obj.tenant = request.user.tenant
        super().save_model(request, obj, form, change)