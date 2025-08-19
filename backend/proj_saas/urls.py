# proj_saas/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import TenantTokenObtainPairView  # Import the tenant login view here

urlpatterns = [
    # Admin site (accessible in all schemas)
    path('admin/', admin.site.urls),
    
    # ===== TENANT SCHEMA ENDPOINTS (tenant1.localhost:8000/) ===== #
    # Tenant Authentication - Defined HERE, not included from users.urls
    path('api/auth/login/', TenantTokenObtainPairView.as_view(), name='tenant-login'),
    
    # Tenant Apps
    path('api/inventory/', include('inventory.urls')),
    path('api/finance/', include('finance.urls')),
    path('api/hrm/', include('hrm.urls')),
    
    # Tenant User Management (other user routes like /api/users/)
    path('api/users/', include('users.urls')),
]