# proj_saas/urls_public.py
from django.contrib import admin

from django.urls import path, include
from users.views import PublicTokenObtainPairView
from core.views import TenantListView, TenantCreateView, TenantDetailView, DomainListView, DomainDetailView

urlpatterns = [
    # ===== PUBLIC SCHEMA ENDPOINTS (localhost:8000/) ===== #
    # Public Authentication
    path('api/auth/login/', PublicTokenObtainPairView.as_view(), name='public-login'),
    
    # Tenant & Domain Management (Superadmin only)
    path('api/tenants/', TenantListView.as_view(), name='tenant-list'),
    path('api/tenants/create/', TenantCreateView.as_view(), name='tenant-create'),
    path('api/tenants/<int:id>/', TenantDetailView.as_view(), name='tenant-detail'),
    path('api/tenants/<int:tenant_id>/domains/', DomainListView.as_view(), name='domain-list'),
    path('api/domains/<int:id>/', DomainDetailView.as_view(), name='domain-detail'),
    
    # Admin site is also accessible from the public domain
    path('admin/', admin.site.urls),
]