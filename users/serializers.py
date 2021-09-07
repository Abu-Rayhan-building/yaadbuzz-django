from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(CustomUser.objects.all())],
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
    )

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
