from rest_framework.permissions import BasePermission
from django.db import connection

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superadmin

class IsTenantAdmin(BasePermission):
    def has_permission(self, request, view):
        tenant = connection.tenant
        return request.user.is_authenticated and request.user.tenantuserrole_set.filter(
            tenant=tenant, role="tenant_admin"
        ).exists()
