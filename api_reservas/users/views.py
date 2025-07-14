from users.models import Perfil
from django.contrib.auth.models import User
from users.serializers import UserSerializer

from rest_framework import generics

class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


