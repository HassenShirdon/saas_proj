from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_tenants.utils import tenant_context, schema_exists
from django.db import transaction
from .models import Tenant, Domain
from .serializers import TenantSerializer, DomainSerializer
# , TenantSignupSerializer
from users.models import User
from rest_framework.permissions import IsAdminUser, AllowAny
import re

class TenantListView(generics.ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        """Superusers see all tenants, staff see only assigned tenants"""
        if self.request.user.is_superuser:
            return Tenant.objects.all()
        return Tenant.objects.filter(pk=self.request.user.tenant_id)

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
        # Use the existing serializer for tenant validation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extract data
        data = serializer.validated_data
        admin_email = request.data.get('admin_email')
        admin_password = request.data.get('admin_password')
        
        # Clean and validate schema name (FIXED)
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
            is_active=data.get('is_active', False),
            max_users=data.get('max_users', 5)
        )
        tenant.save()
        
        # Create domain (default to schema_name.localhost)
        domain_name = request.data.get('domain', f"{schema_name}.localhost")
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
                        email=admin_email,
                        password=admin_password,
                        is_staff=True,
                        is_superuser=True
                    )
            except Exception as e:
                # If user creation fails, we might want to handle this gracefully
                # You can choose to delete the tenant or just log the error
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
            # Generate a default name if empty
            import uuid
            return f"tenant_{uuid.uuid4().hex[:8]}"
        
        # Convert to lowercase
        name = name.lower().strip()
        
        # Replace spaces, hyphens, and other separators with underscores
        name = re.sub(r'[\s\-\.]+', '_', name)
        
        # Remove invalid characters (keep only letters, numbers, underscores)
        name = re.sub(r'[^a-z0-9_]', '', name)
        
        # Remove leading underscores and numbers
        name = re.sub(r'^[0-9_]+', '', name)
        
        # Ensure it starts with a letter
        if name and not name[0].isalpha():
            name = f"t_{name}"
        
        # Ensure it's not too long (PostgreSQL limit is 63 characters)
        if len(name) > 63:
            name = name[:63]
        
        return name
    
    def is_valid_schema_name(self, name):
        """Validate schema name according to PostgreSQL and django-tenants rules"""
        if not name or len(name) < 1:
            return False
        
        # Check if starts with letter
        if not name[0].isalpha():
            return False
        
        # Check if contains only valid characters
        if not re.match(r'^[a-z][a-z0-9_]*$', name):
            return False
        
        # Check if not starting with pg_ (PostgreSQL reserved)
        if name.startswith('pg_'):
            return False
        
        # Check length
        if len(name) > 63:
            return False
        
        return True
# class TenantSignupView(generics.CreateAPIView):
#     serializer_class = TenantSignupSerializer
#     permission_classes = [AllowAny]  # Public access for signup
    
#     @transaction.atomic
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data
        
#         # Validate schema doesn't exist
#         schema_name = data['name'].lower().replace(' ', '-')
#         if schema_exists(schema_name):
#             raise ValidationError({'name': 'Organization name is already taken'})

#         # Validate domain doesn't exist
#         if Domain.objects.filter(domain=data['domain']).exists():
#             raise ValidationError({'domain': 'This domain is already registered'})

#         # Create tenant
#         tenant = Tenant(
#             name=data['name'],
#             schema_name=schema_name,
#             is_active=False,  # Require admin approval
#             max_users=data.get('max_users', 3)
#         )
#         tenant.save()
        
#         # Create domain
#         domain = Domain(
#             domain=data['domain'],
#             tenant=tenant,
#             is_primary=True
#         )
#         domain.save()
        
#         # Create admin user in tenant schema
#         with tenant_context(tenant):
#             try:
#                 User.objects.create_user(
#                     email=data['email'],
#                     password=data['password'],
#                     username=data['email'],
#                     is_staff=True,
#                     is_active=True
#                 )
#             except Exception as e:
#                 raise ValidationError({'user': str(e)})
        
#         return Response({
#             'status': 'success',
#             'message': 'Tenant registered successfully. Awaiting admin approval.',
#             'tenant': TenantSerializer(tenant).data,
#             'domain': DomainSerializer(domain).data
#         }, status=status.HTTP_201_CREATED)

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