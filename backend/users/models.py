from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    is_superadmin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class TenantUserRole(models.Model):
    ROLE_CHOICES = [
        ("tenant_admin", "Tenant Admin"),
        ("manager", "Manager"),
        ("member", "Member"),
    ]

    MODULE_CHOICES = [
        ("hrm", "HRM"),
        ("finance", "Finance"),
        ("inventory", "Inventory"),
        ("operations", "Operations"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tenant = models.ForeignKey('core.Tenant', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    module = models.CharField(max_length=50, choices=MODULE_CHOICES, blank=True, null=True)

    class Meta:
        unique_together = ("user", "tenant", "role", "module")

    def __str__(self):
        return f"{self.user.email} - {self.role} - {self.module or 'all'}"
