from rest_framework import serializers
from .models import User, TenantUserRole
from django_tenants.utils import get_tenant_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

Tenant = get_tenant_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_superadmin"]

class TenantUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUserRole
        fields = ["id", "user", "tenant", "role", "module"]

# JWT Serializer with automatic tenant detection
class AutoTenantTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

class AutoTenantTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # ✅ Allow BOTH Django superusers and your custom superadmins
        if getattr(user, "is_superuser", False) or getattr(user, "is_superadmin", False):
            tenant_info = {"subdomain": "public", "role": "superadmin"}
        else:
            tenant_roles = TenantUserRole.objects.filter(user=user)
            if not tenant_roles.exists():
                raise serializers.ValidationError("User does not belong to any tenant")
            tenant_role = tenant_roles.first()
            tenant_info = {
                "subdomain": tenant_role.tenant.schema_name,
                "role": tenant_role.role
            }

        data.update({"tenant_info": tenant_info})
        return data
