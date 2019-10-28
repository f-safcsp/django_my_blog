from django.urls import path
from .views import (
    UserCreateAPIView,
)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('Singup/', UserCreateAPIView.as_view(), name='user-singup'),   
    path('Login/', obtain_jwt_token, name='user-login'),
]