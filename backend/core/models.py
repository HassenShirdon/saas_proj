from django_tenants.models import TenantMixin, DomainMixin
from django.db import models, connection
from django.core.exceptions import PermissionDenied
import uuid

class Client(TenantMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=63, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    auto_create_schema = True  # Automatically create schema on save

    def save(self, *args, **kwargs):
        if connection.schema_name != 'public':
            raise PermissionDenied("Client model can only be modified in the public schema")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if connection.schema_name != 'public':
            raise PermissionDenied("Client model can only be deleted in the public schema")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    def save(self, *args, **kwargs):
        if connection.schema_name != 'public':
            raise PermissionDenied("Domain model can only be modified in the public schema")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if connection.schema_name != 'public':
            raise PermissionDenied("Domain model can only be deleted in the public schema")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.domain