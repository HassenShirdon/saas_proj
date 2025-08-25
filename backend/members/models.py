from django.conf import settings
from django.db import models

class Member(models.Model):
    class Role(models.TextChoices):
        TENANT_ADMIN = 'TA', 'Tenant Admin'
        FINANCE_MANAGER = 'FM', 'Finance Manager'
        HRM_MANAGER = 'HM', 'HRM Manager'
        INVENTORY_MANAGER = 'IM', 'Inventory Manager'
        FINANCE_MEMBER = 'FE', 'Finance Member'
        HRM_MEMBER = 'HE', 'HRM Member'
        INVENTORY_MEMBER = 'IE', 'Inventory Member'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=Role.choices)
    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role__in': [Role.FINANCE_MANAGER, Role.HRM_MANAGER, Role.INVENTORY_MANAGER]}
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
