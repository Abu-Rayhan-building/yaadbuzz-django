from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, UserPerDepartmentViewsSet

router = DefaultRouter()
router.register(r"departments", DepartmentViewSet)
router.register(
    r"user_per_departments",
    UserPerDepartmentViewsSet,
    basename="UserPerDeparment",
)

urlpatterns = [
    path("", include(router.urls)),
]
