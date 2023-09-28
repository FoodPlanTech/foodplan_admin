from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import TelegramUser
from .serializers import TelegramUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
