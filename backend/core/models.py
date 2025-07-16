from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    auto_create_schema = True

    class Meta:
        ordering = ['name']

class Domain(DomainMixin):
    pass