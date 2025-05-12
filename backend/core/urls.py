# core/urls.py
from django.urls import path
from . import views  # Make sure you have some views to handle requests

urlpatterns = [
    path('', views.home, name='home'),  # This can be the root URL for public schema
    # Add other paths if needed
]
