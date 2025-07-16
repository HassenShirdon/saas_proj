# users/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status

from core.models import Domain

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        tenant = user.tenant

        domain = Domain.objects.filter(tenant=tenant).first()
        domain_url = domain.domain if domain else "localhost:5173"

        data['user'] = {
            'id': user.id,
            'username': user.username,
            'is_superuser': user.is_superuser,
            'is_tenant_admin': getattr(user, 'is_tenant_admin', False),
            'tenant_id':  tenant.id if tenant else None,
            'domain': domain_url  # 👈 sent to Vue for redirect
        }

        return data


class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
