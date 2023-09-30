import random
from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework.exceptions import ValidationError
from .models import Recipe, FoodPlan, Preference
from accounts.models import TelegramAccount
from subscriptions.models import Subscription


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'guide',
            'image',
            'ingredients',
            'preferences',
        )
        depth = 1


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
        )


class FoodPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPlan
        fields = (
            'tg_account',
            'preferences',
        )
        depth = 1


class GetRecipeQuerySerializer(serializers.Serializer):
    telegram_id = serializers.PrimaryKeyRelatedField(
        queryset=TelegramAccount.objects.all(), required=True)

    def create(self, validated_data, request):
        telegram_id = validated_data.get('telegram_id')

        foodplan = FoodPlan.objects.filter(pk=telegram_id) \
            .prefetch_related('preferences')
        if not foodplan:
            raise ValidationError(
                f'FoodPlan для пользователя {telegram_id} не найден.')

        preferences = foodplan[0].preferences.all()
        if not preferences:
            raise ValidationError(
                f'Предпочтения пользователя {telegram_id} не заполнены.')

        recipes = Recipe.objects.filter(preferences__in=preferences)
        recipe = random.choice(recipes)
        return RecipeSerializer(recipe, context={'request': request}).data
