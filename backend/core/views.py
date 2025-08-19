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
        
        # Validate schema doesn't exist
        schema_name = data.get('schema_name', '').lower().replace(' ', '-')
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
            with tenant_context(tenant):
                User.objects.create_user(
                    email=admin_email,
                    password=admin_password,
                    is_staff=True,
                    is_superuser=True
                )
        
        return Response({
            'status': 'success',
            'message': 'Tenant created successfully' + (' with admin user' if admin_email else ''),
            'tenant': TenantSerializer(tenant).data,
            'domain': DomainSerializer(domain).data
        }, status=status.HTTP_201_CREATED)

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