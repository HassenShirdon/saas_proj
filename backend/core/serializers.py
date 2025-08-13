from rest_framework import serializers
from core.models import Tenant, Domain

class TenantSerializer(serializers.ModelSerializer):
    domain = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'schema_name', 'domain']
        read_only_fields = ('id', 'created_on')

    def create(self, validated_data):
        domain_name = validated_data.pop('domain')
        tenant = super().create(validated_data)
        Domain.objects.create(domain=domain_name, tenant=tenant, is_primary=True)
        return tenant