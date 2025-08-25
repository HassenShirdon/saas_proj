# core/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_tenants.utils import tenant_context, schema_exists
from django.db import transaction
from .models import Tenant, Domain
from .serializers import TenantSerializer, DomainSerializer
from users.models import User
from rest_framework.permissions import IsAdminUser
import re
import uuid

class TenantListView(generics.ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        """Superusers see all tenants, tenant admins see only their tenant"""
        if self.request.user.is_superuser:
            return Tenant.objects.all()
        elif hasattr(self.request.user, 'tenant'):
            return Tenant.objects.filter(id=self.request.user.tenant_id)
        return Tenant.objects.none()

class TenantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def perform_destroy(self, instance):
        """Prevent deletion of active tenants"""
        if instance.is_active:
            raise ValidationError("Cannot delete active tenants. Deactivate first.")
        instance.delete()

class TenantCreateView(generics.CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAdminUser]
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response(
                {"error": "Only superusers can create tenants"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Use the existing serializer for tenant validation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extract data
        data = serializer.validated_data
        admin_email = request.data.get('admin_email')
        admin_password = request.data.get('admin_password')
        admin_username = request.data.get('admin_username', admin_email)
        domain_name = request.data.get('domain_name')
        
        # Clean and validate schema name
        schema_name = self.clean_schema_name(data.get('schema_name', ''))
        
        # Validate schema name format
        if not self.is_valid_schema_name(schema_name):
            raise ValidationError("Invalid schema name. Must start with a letter and contain only letters, numbers, and underscores.")
        
        # Validate schema doesn't exist
        if schema_exists(schema_name):
            raise ValidationError("Tenant with this schema name already exists")

        # Create tenant
        tenant = Tenant(
            schema_name=schema_name,
            tenant_name=data.get('tenant_name'),
            address=data.get('address', ''),
            is_active=data.get('is_active', True),
            max_users=data.get('max_users', 10)
        )
        tenant.save()
        
        # Create domain
        domain_name = domain_name or f"{schema_name}.localhost"
        if Domain.objects.filter(domain=domain_name).exists():
            raise ValidationError("Domain already exists")
            
        domain = Domain(
            domain=domain_name,
            tenant=tenant,
            is_primary=True
        )
        domain.save()
        
        # Create admin user in tenant schema if credentials provided
        if admin_email and admin_password:
            try:
                with tenant_context(tenant):
                    User.objects.create_user(
                        username=admin_username,
                        email=admin_email,
                        password=admin_password,
                        first_name=request.data.get('admin_first_name', ''),
                        last_name=request.data.get('admin_last_name', ''),
                        tenant=tenant,
                        role=User.Role.TENANT_ADMIN,
                        is_staff=True
                    )
            except Exception as e:
                raise ValidationError(f"Failed to create admin user: {str(e)}")
        
        return Response({
            'status': 'success',
            'message': 'Tenant created successfully' + (' with admin user' if admin_email else ''),
            'tenant': TenantSerializer(tenant).data,
            'domain': DomainSerializer(domain).data
        }, status=status.HTTP_201_CREATED)
    
    def clean_schema_name(self, name):
        """Clean and format schema name to be PostgreSQL compatible"""
        if not name:
            return f"tenant_{uuid.uuid4().hex[:8]}"
        
        name = name.lower().strip()
        name = re.sub(r'[\s\-\.]+', '_', name)
        name = re.sub(r'[^a-z0-9_]', '', name)
        name = re.sub(r'^[0-9_]+', '', name)
        
        if name and not name[0].isalpha():
            name = f"t_{name}"
        
        if len(name) > 63:
            name = name[:63]
        
        return name
    
    def is_valid_schema_name(self, name):
        if not name or len(name) < 1:
            return False
        
        if not name[0].isalpha():
            return False
        
        if not re.match(r'^[a-z][a-z0-9_]*$', name):
            return False
        
        if name.startswith('pg_'):
            return False
        
        if len(name) > 63:
            return False
        
        return True

class DomainListView(generics.ListCreateAPIView):
    serializer_class = DomainSerializer
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        return Domain.objects.filter(tenant_id=self.kwargs['tenant_id'])
    
    def perform_create(self, serializer):
        tenant = Tenant.objects.get(pk=self.kwargs['tenant_id'])
        serializer.save(tenant=tenant)

class DomainDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'