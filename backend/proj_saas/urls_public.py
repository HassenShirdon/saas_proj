# proj_saas/urls_public.py
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from django.urls import path, include

urlpatterns = [
    # ===== PUBLIC SCHEMA ENDPOINTS (localhost:8000/) ===== #
    
    # Admin site is also accessible from the public domain
    path('admin/', admin.site.urls),
    # Public Authentication
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Users Management 
    path('api/users/', include('users.urls')),
    # Tenant & Domain Management (Superadmin only)
    path('api/',include('core.urls')),
    
]