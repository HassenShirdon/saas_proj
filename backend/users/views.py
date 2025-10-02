from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, TenantUserRole
from .serializers import UserSerializer, TenantUserRoleSerializer, AutoTenantTokenObtainPairSerializer
from .permissions import IsSuperAdmin, IsTenantAdmin
from rest_framework_simplejwt.views import TokenObtainPairView
from django_tenants.utils import get_tenant_model

Tenant = get_tenant_model()

# JWT login
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = AutoTenantTokenObtainPairSerializer

# Superadmin endpoints
class TenantAdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.filter(tenantuserrole__role='tenant_admin')

    def create(self, request, *args, **kwargs):
        tenant_id = request.data.get("tenant_id")
        password = request.data.get("password")
        email = request.data.get("email")
        username = request.data.get("username")

        if not all([tenant_id, password, email, username]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        tenant = Tenant.objects.get(id=tenant_id)
        user = User.objects.create_user(username=username, email=email, password=password)
        TenantUserRole.objects.create(user=user, tenant=tenant, role="tenant_admin")
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Tenant admin endpoints
class ManagerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsTenantAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.filter(tenantuserrole__role='manager')

    def create(self, request, *args, **kwargs):
        modules = request.data.get("modules", [])
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")

        if not all([email, username, password]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        tenant = request.user.tenantuserrole_set.get(role="tenant_admin").tenant

        for module in modules:
            TenantUserRole.objects.create(user=user, tenant=tenant, role="manager", module=module)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsTenantAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.filter(tenantuserrole__role='member')

    def create(self, request, *args, **kwargs):
        modules = request.data.get("modules", [])
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")

        if not all([email, username, password]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        tenant = request.user.tenantuserrole_set.get(role="tenant_admin").tenant

        for module in modules:
            TenantUserRole.objects.create(user=user, tenant=tenant, role="member", module=module)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
