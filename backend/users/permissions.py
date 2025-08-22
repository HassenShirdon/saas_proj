from rest_framework import permissions

class IsTenantMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request, 'tenant'):
            return False
        tenant = request.tenant
        return request.user.tenants.filter(id=tenant.id).exists()

class HasGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        required_groups = getattr(view, 'required_groups', [])
        if not required_groups:
            return True
        return any(request.user.groups.filter(name=group).exists() for group in required_groups)