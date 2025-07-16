# proj_saas/urls_public.py
from django.urls import path, include
from django.contrib import admin
from users.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Allow login from public schema
    path('api/core/', include('core.urls')),   # Manage tenants from here
    path('api/token/', CustomLoginView.as_view(), name='token_obtain_pair'),
]
