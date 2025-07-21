from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from tenant_users.tenants.utils import get_tenant_model
from django.conf import settings
from .serializers import CustomUserSerializer

Client = get_tenant_model()

class LoginRedirectAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        if hasattr(user, "tenants") and user.tenants.exists():
            tenant = user.tenants.first()
            domain_obj = tenant.domains.first()
            redirect_url = f"https://{domain_obj.domain}/"
        else:
            redirect_url = f"https://{settings.PUBLIC_DOMAIN}/"

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": CustomUserSerializer(user).data,
            "redirect_url": redirect_url,
        })
