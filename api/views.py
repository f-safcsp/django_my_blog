from django.shortcuts import render
from .serializers import (
    UserCreateSerializer,
    UserUpdateSerializer
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView
)
from django.contrib.auth.models import User 

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer 
    permission_classes = [AllowAny]

class UserUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer 
    queryset = User.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'
    permission_classes = [IsAuthenticated] 