from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema

from yearbook.permissions import IsOwner
from yearbook.models import Department, UserPerDepartment
from yearbook.serializers import (
    DepartmentJoinSerializer,
    DepartmentSerializer,
    UserPerDepartmentSerializer,
)

# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        return query.filter(owner=request.user)

    @extend_schema(request=DepartmentJoinSerializer)
    @action(detail=True, methods=["post"], permission_classes=(IsAuthenticated,))
    def join(self, request, pk=None):
        department = self.get_object()
        serializer = DepartmentJoinSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if (
            not department.is_join_allowed
            or serializer.validated_data["password"] != department.join_password
        ):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user_per_dept = UserPerDepartment(
            user=request.user.profile, department=department
        )
        user_per_dept.save()

        return Response(
            data=DepartmentSerializer(department).data,
            status=status.HTTP_200_OK,
        )


class UserPerDepartmentViewsSet(viewsets.ModelViewSet):
    queryset = UserPerDepartment.objects.none()
    serializer_class = UserPerDepartmentSerializer
    http_method_names = ["get", "put", "head"]
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return UserPerDepartment.objects(user=self.request.user)
