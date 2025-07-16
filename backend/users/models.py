from django.contrib.auth.models import AbstractUser
from django.db import models
from django_tenants.utils import get_tenant_model

class CustomUser(AbstractUser):
    is_tenant_admin = models.BooleanField(default=False)
    tenant = models.ForeignKey(
    'core.Client',  # or whatever your tenant model is
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    class Meta:
        permissions = [
            ("manage_users", "Can manage tenant users"),
        ]
    