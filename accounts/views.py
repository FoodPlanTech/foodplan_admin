from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import TelegramAccount
from .serializers import UserSerializer, TelegramAccountSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class TelegramAccountViewSet(viewsets.ModelViewSet):
    queryset = TelegramAccount.objects.all()
    serializer_class = TelegramAccountSerializer
