# users/urls.py
from django.urls import path
from .views import UserCreateAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    # User Management (Tenant Schema Only)
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]