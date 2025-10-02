from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import MultipleObjectsReturned
from users.models import TenantUserRole
from django.db import connection

User = get_user_model()


class TenantAwareAuthBackend(BaseBackend):
    """
    Custom authentication backend to allow login with email/password,
    auto-detect the tenant for the user.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        email = username or kwargs.get('email')
        if not email or not password:
            return None

        try:
            # Search in public schema
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            # Should not happen if email is unique
            return None

        # Check password
        if not user.check_password(password):
            return None

        # If superadmin, no tenant check needed
        if user.is_superadmin:
            return user

        # Check if user is linked to at least one tenant
        tenant_roles = TenantUserRole.objects.filter(user=user)
        if not tenant_roles.exists():
            return None  # User not assigned to any tenant

        # Optionally: store primary tenant in user object for later access
        request.tenant = tenant_roles.first().tenant if request else None

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
