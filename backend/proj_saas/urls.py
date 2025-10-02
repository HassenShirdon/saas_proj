# proj_saas/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import CustomTokenObtainPairView

urlpatterns = [
    # ===== Admin site ===== #
    path('admin/', admin.site.urls),

    # ===== JWT Authentication (Superadmin & Tenant users) ===== #
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # ===== Core app (tenant management: public schema only) ===== #
    path('api/', include('core.urls')),

    # ===== Users app ===== #
    # Superadmin endpoints: create tenant admins (public schema)
    # Tenant Admin endpoints: create managers/members (tenant schemas)
    path('api/users/', include('users.urls')),

    # ===== Tenant-specific apps ===== #
    path('api/inventory/', include('inventory.urls')),
    path('api/finance/', include('finance.urls')),
    path('api/hrm/', include('hrm.urls')),
    
]
