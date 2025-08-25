# core/serializers.py
from rest_framework import serializers
from .models import Tenant, Domain
import re 

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'

class TenantSerializer(serializers.ModelSerializer):
    domains = DomainSerializer(many=True, read_only=True)
    user_count = serializers.SerializerMethodField(read_only=True)
    admin_email = serializers.EmailField(write_only=True, required=False)
    admin_password = serializers.CharField(write_only=True, required=False, min_length=8)
    admin_username = serializers.CharField(write_only=True, required=False)
    domain_name = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Tenant
        fields = [
            'id', 'schema_name', 'tenant_name', 'address', 'created_on', 
            'is_active', 'max_users', 'domains', 'user_count',
            'admin_email', 'admin_password', 'admin_username', 'domain_name'
        ]
        read_only_fields = ('id', 'schema_name', 'created_on', 'domains', 'user_count')
    
    def get_user_count(self, obj):
        return obj.get_user_count()
    
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