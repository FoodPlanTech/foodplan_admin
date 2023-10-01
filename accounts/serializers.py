from rest_framework import serializers

from .models import TelegramAccount


class TelegramAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramAccount
        fields = (
            'telegram_id',
            'user',
            'created_at',
        )
