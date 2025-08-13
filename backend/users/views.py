from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from .permissions import IsTenantAdmin, IsTenantUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsTenantAdmin | permissions.IsAdminUser]
    
    def get_queryset(self):
        # Tenant admins can only see users from their tenant
        if self.request.user.is_tenant_admin:
            return CustomUser.objects.filter(tenant=self.request.user.tenant)
        return super().get_queryset()
    
    def perform_create(self, serializer):
        # Automatically set the tenant to the current user's tenant
        serializer.save(tenant=self.request.user.tenant)
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsTenantUser()]
        return super().get_permissions()