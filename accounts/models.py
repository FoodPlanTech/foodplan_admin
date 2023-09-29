from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ...


class TelegramAccount(models.Model):
    """
    Draft user model with only Telegram ID. Will be attached to User when the
    user will buy subscription.
    """
    telegram_id = models.BigIntegerField('Telegram ID', unique=True)
    created_at = models.DateTimeField('Добавлен', auto_now_add=True)
    user = models.OneToOneField(CustomUser, related_name='telegram',
                                on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.telegram_id)
