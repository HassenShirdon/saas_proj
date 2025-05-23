
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),  # auth-related routes
    path('', include('core.urls')),
    path('inventory/', include('inventory.urls')),
    path('finance/', include('finance.urls')),
]

