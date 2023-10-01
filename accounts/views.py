from rest_framework import generics

from .models import TelegramAccount
from .serializers import TelegramAccountSerializer


class TelegramAccountCreateViewSet(generics.CreateAPIView):
    """Добавить новый Телеграмм-аккаунт в базу (только POST-запрос)."""
    queryset = TelegramAccount.objects.all()
    serializer_class = TelegramAccountSerializer
