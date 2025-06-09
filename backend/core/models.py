from django_tenants.models import TenantMixin, DomainMixin
from django.db import models, connection
from django.core.exceptions import PermissionDenied

class Client(TenantMixin):
    name = models.CharField(max_length=100)
   

    def save(self, *args, **kwargs):
        if connection.schema_name != 'public':
            raise PermissionDenied("Client model can only be modified in the public schema")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if connection.schema_name != 'public':
            raise PermissionDenied("Client model can only be deleted in the public schema")
        super().delete(*args, **kwargs)

class Domain(DomainMixin):
    def save(self, *args, **kwargs):
        if connection.schema_name != 'public':
            raise PermissionDenied("Domain model can only be modified in the public schema")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if connection.schema_name != 'public':
            raise PermissionDenied("Domain model can only be deleted in the public schema")
        super().delete(*args, **kwargs)