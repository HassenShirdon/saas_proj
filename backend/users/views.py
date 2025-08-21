from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django_tenants.utils import get_tenant_model, get_public_schema_name
from .models import User
from .serializers import UserSerializer, UserCreateSerializer

def get_tenant_from_request(request):
    TenantModel = get_tenant_model()
    hostname = request.get_host().split(':')[0]
    
    # Handle localhost and public schema
    if hostname in ['localhost', '127.0.0.1']:
        return TenantModel.objects.get(schema_name=get_public_schema_name())
    
    # Extract subdomain for tenant schemas (e.g., tenant1.localhost -> tenant1)
    parts = hostname.split('.')
    if len(parts) >= 2:
        subdomain = parts[0]
        try:
            return TenantModel.objects.get(schema_name=subdomain)
        except TenantModel.DoesNotExist:
            raise Exception(f"Tenant '{subdomain}' not found")
    
    # If we can't parse the hostname properly
    raise Exception(f"Invalid hostname format: {hostname}")

class PublicTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            tenant = get_tenant_from_request(request)
            if tenant.schema_name != get_public_schema_name():
                return Response(
                    {"detail": "Public login only accessible via public schema (localhost:8000)"}, 
                    status=status.HTTP_403_FORBIDDEN
                )
        except Exception as e:
            return Response(
                {"detail": f"Schema error: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().post(request, *args, **kwargs)

class TenantTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            tenant = get_tenant_from_request(request)
            if tenant.schema_name == get_public_schema_name():
                return Response(
                    {"detail": "Tenant login only accessible via tenant schemas (tenant1.localhost:8000)"}, 
                    status=status.HTTP_403_FORBIDDEN
                )
        except Exception as e:
            return Response(
                {"detail": f"Schema error: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().post(request, *args, **kwargs)

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        tenant = get_tenant_from_request(self.request)
        serializer.save(tenant=tenant)

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = get_tenant_from_request(self.request)
        return User.objects.filter(tenant=tenant)

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    # REMOVE the generic queryset: queryset = User.objects.all()

    def get_queryset(self):
        # Add the same tenant filtering as in UserListAPIView
        tenant = get_tenant_from_request(self.request)
        return User.objects.filter(tenant=tenant)