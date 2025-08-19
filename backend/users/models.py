from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from core.models import Tenant

class UserManager(BaseUserManager):
    """Custom user manager using email instead of username"""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    # Remove username, use email as primary identifier
    username = None
    email = models.EmailField(unique=True)
    
    # Tenant relationship - each user belongs to a specific tenant
    tenant = models.ForeignKey(
        Tenant, 
        on_delete=models.CASCADE, 
        related_name='users',
        null=True,  # Allow null for superusers in public schema
        blank=True
    )
    
    # Additional fields
    phone_number = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    # Authentication fields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # No additional required fields
    
    # ADD THIS LINE - Use the custom manager
    objects = UserManager()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tenant', 'email'],
                name='unique_email_per_tenant'
            )
        ]
    
    def __str__(self):
        return self.email