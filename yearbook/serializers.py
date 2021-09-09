from rest_framework import serializers

from .models import Department, UserPerDepartment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name", "join_password", "is_join_allowed", "id"]
        read_only_fields = ["id"]


class DepartmentJoinSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, max_length=50)


class UserPerDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPerDepartment
        fields = ["id", "user", "department", "bio", "avatar", "nickname"]
        read_only_fields = ["id", "user", "department"]
