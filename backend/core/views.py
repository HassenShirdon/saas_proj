from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny  # Can replace later with IsSuperAdmin
from .models import Tenant, Domain
from .serializers import TenantSerializer
from rest_framework.permissions import AllowAny

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [AllowAny]  # Replace with custom permission if needed

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)