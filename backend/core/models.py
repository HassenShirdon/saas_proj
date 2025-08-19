from django_tenants.models import TenantMixin, DomainMixin
from django.db import models
from django_tenants.utils import get_public_schema_name

class Tenant(TenantMixin):
    tenant_name = models.CharField(max_length=100)
    address = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    max_users = models.IntegerField(default=4)
    
    auto_create_schema = True
    auto_drop_schema = True
    
    def __str__(self):
        return self.tenant_name
    
    def is_public(self):
        return self.schema_name == get_public_schema_name()

class Domain(DomainMixin):
    def __str__(self):
        return self.domain