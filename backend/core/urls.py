# core/urls.py
from django.urls import path
from .views import (
    TenantListView, TenantCreateView, TenantDetailView,
    DomainListView, DomainDetailView
)

urlpatterns = [
    # Tenant management
    path('tenants/', TenantListView.as_view(), name='tenant-list'),
    path('tenants/create/', TenantCreateView.as_view(), name='tenant-create'),
    path('tenants/<int:id>/', TenantDetailView.as_view(), name='tenant-detail'),
    
    # Domain management
    path('tenants/<int:tenant_id>/domains/', DomainListView.as_view(), name='domain-list'),
    path('domains/<int:id>/', DomainDetailView.as_view(), name='domain-detail'),
]