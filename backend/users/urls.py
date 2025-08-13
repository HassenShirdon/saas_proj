from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from djoser.views import UserViewSet as DjoserUserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns =[
    path('users/me/', DjoserUserViewSet.as_view({'get': 'me'})),

] + router.urls

