from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomTokenObtainPairView, TenantAdminViewSet, ManagerViewSet, MemberViewSet

router = DefaultRouter()
router.register(r"superadmin/tenant-admins", TenantAdminViewSet, basename="tenant-admin")
router.register(r"tenant-admin/managers", ManagerViewSet, basename="manager")
router.register(r"tenant-admin/members", MemberViewSet, basename="member")

urlpatterns = [
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("", include(router.urls)),
]
