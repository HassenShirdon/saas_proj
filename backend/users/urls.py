from django.urls import path
from .views import LoginRedirectAPIView

urlpatterns = [
    path("token/", LoginRedirectAPIView.as_view(), name="login-redirect"),
]
