from django.urls import path
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='token_obtain_pair'),
]
