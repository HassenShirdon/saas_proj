from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'date_joined']
        read_only_fields = ['id', 'is_active', 'date_joined']

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'role', 'tenant']
    
    def validate(self, attrs):
        request = self.context.get('request')
        
        if request and hasattr(request, 'user'):
            if not request.user.is_tenant_admin:
                raise serializers.ValidationError("Only tenant admins can create users")
            
            # Tenant admins can only create users for their own tenant
            attrs['tenant'] = request.user.tenant
            
            # Prevent creating other tenant admins
            if attrs.get('role') == 'TENANT_ADMIN':
                raise serializers.ValidationError("Cannot create tenant admin users")
        
        return super().validate(attrs)