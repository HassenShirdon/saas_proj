from django.urls import path
from .views import UserRegisterView, UserListView, UserDetailView, TenantAdminCreateView

urlpatterns = [
    path('create/', UserRegisterView.as_view(), name='user_register'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('tenant-admin/', TenantAdminCreateView.as_view(), name='tenant_admin_create'),
]