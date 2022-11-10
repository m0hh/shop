from rest_framework import generics
from user.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class UserReg(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
