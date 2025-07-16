from django_tenants.utils import schema_context
from django_tenants.middleware.main import TenantMainMiddleware

from django.urls import path, include

urlpatterns = [
    path('api/inventory/', include('inventory.urls')),
    path('api/finance/', include('finance.urls')),
    path('api/hrm/', include('hrm.urls')),
    path('api/users/', include('users.urls')),
]