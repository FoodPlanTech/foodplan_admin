from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import TelegramUser


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


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = (
            'id',
            'telegram_id',
            'created_at',
        )
