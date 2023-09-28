from django.contrib.auth.models import AbstractUser
from django.db import models


class TelegramUser(models.Model):
    """
    Draft user model with only Telegram ID. Will be attached to User when the
    user will buy subscription.
    """
    telegram_id = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telegram_id


class CustomUser(AbstractUser):
    telegram = models.OneToOneField(TelegramUser, related_name='user',
                                    on_delete=models.CASCADE, null=True)
