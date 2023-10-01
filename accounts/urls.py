from django.urls import path

from .views import TelegramAccountCreateViewSet

urlpatterns = [
    path('tg-accounts/', TelegramAccountCreateViewSet.as_view(), name='tg-accounts'),
]
