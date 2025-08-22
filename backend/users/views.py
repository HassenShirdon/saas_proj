from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .permissions import IsTenantMember, HasGroupPermission

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsTenantMember, HasGroupPermission]
    required_groups = ['finance_manager', 'hrm_manager', 'operation_manager']

    def get_queryset(self):
        tenant = getattr(self.request, 'tenant', None)
        if tenant and tenant.schema_name != 'public':
            return User.objects.filter(tenants=tenant)
        return User.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsTenantMember]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAuthenticated, IsTenantMember, HasGroupPermission]
            self.required_groups = ['finance_manager', 'hrm_manager', 'operation_manager']
        return super().get_permissions()

    def get_queryset(self):
        tenant = getattr(self.request, 'tenant', None)
        user = self.request.user
        if tenant and tenant.schema_name != 'public':
            if user.groups.filter(name__in=['finance_manager', 'hrm_manager', 'operation_manager']).exists():
                return User.objects.filter(tenants=tenant)
            return User.objects.filter(id=user.id, tenants=tenant)
        return User.objects.filter(id=user.id)

class TenantAdminCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(is_staff=True)