from users.serializers import RegisterSerializer
from users.models import CustomUser
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics, serializers

# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
