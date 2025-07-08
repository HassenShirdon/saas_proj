from django.urls import path
from .views import ClientViewSet

urlpatterns = [
    path('clients', ClientViewSet.as_view({'get': 'list', 'post': 'create'}), name='client-list'),
    path('client/<int:pk>/', ClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-detail'),
    path('client/<int:pk>/activate/', ClientViewSet.as_view({'post': 'activate'}), name='client-activate'),
    path('client/<int:pk>/deactivate/', ClientViewSet.as_view({'post': 'deactivate'}), name='client-deactivate'),
]