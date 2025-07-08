from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAdminUser
from .models import Client
from .serializers import ClientSerializer
from django_tenants.utils import tenant_context
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import connection

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]  # Only superusers can access

    def get_queryset(self):
        if connection.schema_name != 'public':
            return Client.objects.none()  # Restrict to public schema
        return super().get_queryset()

    def perform_create(self, serializer):
        with tenant_context(self.request.tenant):
            instance = serializer.save()
            return instance

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def activate(self, request, pk=None):
        client = self.get_object()
        client.is_active = True
        client.save()
        return Response({'status': 'Tenant activated'})

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def deactivate(self, request, pk=None):
        client = self.get_object()
        client.is_active = False
        client.save()
        return Response({'status': 'Tenant deactivated'})