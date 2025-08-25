from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Tenant, Domain
from .serializers import UserSerializer, UserCreateSerializer, TenantSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "create_tenant_admin"]:
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ["list", "destroy", "create_tenant_admin", "create_tenant"]:
            permission_classes = [permissions.IsAdminUser]  # superuser only
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)

    # Login endpoint
    @action(detail=False, methods=["post"], permission_classes=[permissions.AllowAny])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful"})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # Logout endpoint
    @action(detail=False, methods=["post"])
    def logout(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"})

    # Superuser creates a tenant
    @action(detail=False, methods=["post"])
    def create_tenant(self, request):
        serializer = TenantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tenant = serializer.save()
        # You should also create a Domain for tenant (example)
        Domain.objects.create(domain=f"{tenant.schema_name}.localhost", tenant=tenant, is_primary=True)
        return Response({"message": "Tenant created", "tenant": serializer.data})

    # Superuser creates a Tenant Admin user
    @action(detail=False, methods=["post"])
    def create_tenant_admin(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Link user to tenant through Member
        tenant_id = request.data.get("tenant_id")
        from members.models import Member
        tenant = Tenant.objects.get(id=tenant_id)
        Member.objects.create(user=user, role=Member.Role.TENANT_ADMIN, tenant=tenant)
        return Response({"message": "Tenant Admin created", "user_id": user.id})
