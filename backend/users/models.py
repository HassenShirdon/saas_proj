from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields later (e.g. tenant, company, etc.)
    pass
