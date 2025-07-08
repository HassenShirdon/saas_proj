from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError
from django_tenants.utils import get_tenant_model

User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    groups = GroupSerializer(many=True, required=False)
    user_permissions = PermissionSerializer(many=True, required=False)
    tenant_admin = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'tenant_admin', 'groups', 'user_permissions']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate(self, data):
        # Ensure tenant_admin users can only be created by tenant admins
        if data.get('tenant_admin') and not self.context['request'].user.tenant_admin:
            raise serializers.ValidationError("Only tenant admins can create tenant admins.")
        return data

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        permissions_data = validated_data.pop('user_permissions', [])
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            tenant_admin=validated_data.get('tenant_admin', False),
            created_by=self.context['request'].user
        )
        # Assign groups
        for group_data in groups_data:
            group = Group.objects.get(name=group_data['name'])
            user.groups.add(group)
        # Assign permissions
        for perm_data in permissions_data:
            permission = Permission.objects.get(codename=perm_data['codename'])
            user.user_permissions.add(permission)
        return user

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, required=False)
    user_permissions = PermissionSerializer(many=True, required=False)
    tenant_admin = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tenant_admin', 'groups', 'user_permissions', 'created_by']

    def update(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        permissions_data = validated_data.pop('user_permissions', [])
        user = super().update(validated_data)
        # Update groups
        if groups_data:
            user.groups.clear()
            for group_data in groups_data:
                group = Group.objects.get(name=group_data['name'])
                user.groups.add(group)
        # Update permissions
        if permissions_data:
            user.user_permissions.clear()
            for perm_data in permissions_data:
                permission = Permission.objects.get(codename=perm_data['codename'])
                user.user_permissions.add(permission)
        return user