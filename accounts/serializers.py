from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import TelegramAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'telegram',
            'first_name',
            'last_name',
            'email',
            'liked_recipes',
            'disliked_recipes',
        )


class TelegramAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramAccount
        fields = (
            'telegram_id',
            'user',
            'created_at',
        )
