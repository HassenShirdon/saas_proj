from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer, MemberCreateSerializer

class IsTenantAdmin(permissions.BasePermission):
    """
    Allows access only to Tenant Admins.
    Assumes user is linked via Member.role
    """

    def has_permission(self, request, view):
        try:
            return request.user.member_set.filter(role='TA').exists() or request.user.is_superuser
        except:
            return False


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsTenantAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Member.objects.all()
        # Tenant Admins see members only of their tenant
        tenant_admin_member = Member.objects.filter(user=user, role='TA').first()
        if tenant_admin_member:
            return Member.objects.filter(manager__isnull=True) | Member.objects.filter(manager=tenant_admin_member)
        return Member.objects.none()

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return MemberCreateSerializer
        return MemberSerializer
