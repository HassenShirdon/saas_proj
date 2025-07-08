from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    tenant_admin = models.BooleanField(default=False)  # Indicates if user is a tenant admin
    created_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_users'
    )  # Tracks who created the user

    class Meta:
        db_table = 'custom_user'  # Ensure consistent table name across tenant schemas

    def __str__(self):
        return f"{self.username} ({self.email})"