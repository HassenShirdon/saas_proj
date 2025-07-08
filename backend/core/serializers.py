from rest_framework import serializers
from .models import Client, Domain

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['domain', 'is_primary']

class ClientSerializer(serializers.ModelSerializer):
    domains = DomainSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'schema_name', 'created_at', 'is_active', 'domains']

    def validate_schema_name(self, value):
        if not value.islower():
            raise serializers.ValidationError("Schema name must be lowercase.")
        if value == 'public':
            raise serializers.ValidationError("Schema name 'public' is reserved.")
        return value

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        # Create a default domain
        Domain.objects.create(
            domain=f"{client.schema_name}.localhost",  # Replace 'localhost' with your base domain in production
            tenant=client,
            is_primary=True
        )
        client.create_schema()
        return client