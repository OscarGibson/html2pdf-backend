from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from applications.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]
