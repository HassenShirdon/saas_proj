# proj_saas/urls_tenant.py (REVISED)
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # ===== TENANT SCHEMA ENDPOINTS (tenant1.localhost:8000/) ===== #
    
    # Admin site
    path('admin/', admin.site.urls),
    
    # Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Users management (tenant-specific operations)
    path('api/users/', include('users.urls')),
    
    # Tenant apps
    path('api/inventory/', include('inventory.urls')),
    path('api/finance/', include('finance.urls')),
    path('api/hrm/', include('hrm.urls')),
    path('api/members/', include('members.urls')),
]