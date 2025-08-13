from django.urls import path, include
from core.views import TenantRegistrationView
from users.views import UserRegistrationView

urlpatterns = [
    path('api/core/register/', TenantRegistrationView.as_view(), name='tenant-register'),
    path('api/auth/register/', UserRegistrationView.as_view(), name='public-user-register'),
]
