from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        extra_fields.setdefault("is_verified", False)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("The Email must be set")
        user = self.create_user(
            email=email,
            password=password,
            is_verified=True,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        return user
