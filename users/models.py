from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
