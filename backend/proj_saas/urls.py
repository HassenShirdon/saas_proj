from django_tenants.utils import schema_context
from django_tenants.middleware.main import TenantMainMiddleware
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from users.views import LoginRedirectAPIView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), # Allow login from public schema
    path('api/core/', include('core.urls')),   # Manage tenants from here
    path('api/inventory/', include('inventory.urls')),
    path('api/finance/', include('finance.urls')),
    path('api/hrm/', include('hrm.urls')),
    path('api/token/', LoginRedirectAPIView.as_view(), name='token_obtain_pair'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/users/', include('users.urls')),
]