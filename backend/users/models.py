from django.contrib.auth.models import AbstractUser
from django.db import models
from django_tenants.models import TenantMixin
from core.models import Tenant

class CustomUser(AbstractUser):
    ROLES = (
        ('TENANT_ADMIN', 'Tenant Administrator'),
        ('FINANCE_MANAGER', 'Finance Manager'),
        ('HR_MANAGER', 'HR Manager'),
        ('OPERATIONS_MANAGER', 'Operations Manager'),
    )
    
    username = None
    email = models.EmailField(unique=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='users')
    role = models.CharField(max_length=20, choices=ROLES)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tenant', 'role']
    
    def __str__(self):
        return f"{self.email} ({self.tenant.name})"
    
    @property
    def is_tenant_admin(self):
        return self.role == 'TENANT_ADMIN'
    
    @property
    def is_finance_manager(self):
        return self.role == 'FINANCE_MANAGER'
    
    @property
    def is_hr_manager(self):
        return self.role == 'HR_MANAGER'
    
    @property
    def is_operations_manager(self):
        return self.role == 'OPERATIONS_MANAGER'

    class Meta:
        unique_together = ('email', 'tenant')