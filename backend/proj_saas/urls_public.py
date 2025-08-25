# proj_saas/urls_public.py (REVISED)
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include

urlpatterns = [
    # ===== PUBLIC SCHEMA ENDPOINTS (localhost:8000/) ===== #
    
    # Admin site
    path('admin/', admin.site.urls),
    
    # Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Core app (tenant management)
    path('api/', include('core.urls')),
    
    # Users management (public schema operations)
    path('api/users/', include('users.urls')),
]