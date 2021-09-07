from rest_framework import serializers

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name", "join_password", "is_join_allowed", "id"]
        read_only_fields = ["id"]


class DepartmentJoinSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, max_length=50)
