from rest_framework import serializers
from .models import Tenant, Domain
import re 

class TenantSerializer(serializers.ModelSerializer):
    admin_email = serializers.EmailField(write_only=True, required=False)
    admin_password = serializers.CharField(write_only=True, required=False, min_length=8)
    domain = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Tenant
        fields = '__all__'
        read_only_fields = ('schema_name', 'created_on')
        extra_fields = ['admin_email', 'admin_password', 'domain']

    def validate_schema_name(self, value):
        """Validate and clean schema name"""
        if not value:
            raise serializers.ValidationError("Schema name is required.")
        
        # Clean the schema name
        value = value.lower().strip()
        value = re.sub(r'[\s\-\.]+', '_', value)
        value = re.sub(r'[^a-z0-9_]', '', value)
        value = re.sub(r'^[0-9_]+', '', value)
        
        # Ensure it starts with a letter
        if value and not value[0].isalpha():
            value = f"t_{value}"
        
        # Final validation
        if not re.match(r'^[a-z][a-z0-9_]*$', value):
            raise serializers.ValidationError(
                "Schema name must start with a letter and contain only letters, numbers, and underscores."
            )
        
        if value.startswith('pg_'):
            raise serializers.ValidationError("Schema name cannot start with 'pg_'.")
        
        if len(value) > 63:
            raise serializers.ValidationError("Schema name cannot exceed 63 characters.")
        
        return value    

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