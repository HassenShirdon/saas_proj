from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from core.models import Tenant

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    tenants = serializers.SlugRelatedField(
        many=True, slug_field='tenant_name', queryset=Tenant.objects.all(), required=False
    )
    groups = serializers.SlugRelatedField(
        many=True, slug_field='name', queryset=Group.objects.all(), required=False
    )
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'tenants', 'groups', 'password', 'is_staff']
        read_only_fields = ['id']

    def create(self, validated_data):
        tenants = validated_data.pop('tenants', [])
        groups = validated_data.pop('groups', [])
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data, password=password)
        user.tenants.set(tenants)
        user.groups.set(groups)
        return user

    def update(self, instance, validated_data):
        tenants = validated_data.pop('tenants', None)
        groups = validated_data.pop('groups', None)
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
        if tenants is not None:
            instance.tenants.set(tenants)
        if groups is not None:
            instance.groups.set(groups)
        
        instance.save()
        return instance