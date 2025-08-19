from rest_framework import serializers
from .models import Tenant, Domain

class TenantSerializer(serializers.ModelSerializer):
    admin_email = serializers.EmailField(write_only=True, required=False)
    admin_password = serializers.CharField(write_only=True, required=False, min_length=8)
    domain = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Tenant
        fields = '__all__'
        read_only_fields = ('schema_name', 'created_on')
        extra_fields = ['admin_email', 'admin_password', 'domain']

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'

# class TenantSignupSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     domain = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)
    
#     def validate_domain(self, value):
#         if Domain.objects.filter(domain=value).exists():
#             raise serializers.ValidationError("Domain already exists")
#         return value