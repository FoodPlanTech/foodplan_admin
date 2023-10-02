import random
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import TelegramAccount
from accounts.serializers import TelegramAccountSerializer

from .models import FoodPlan, Recipe


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


class CreateLikeSerializer(serializers.Serializer):
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(), required=True)
    telegram_id = serializers.PrimaryKeyRelatedField(
        queryset=TelegramAccount.objects.all(), required=True)

    def update(self, validated_data, is_dislike=False):
        recipe_id = validated_data.get('recipe_id')
        telegram_id = validated_data.get('telegram_id')

        try:
            # TODO:
            # - отлайкнуть/отдизлайкнть обратно;
            # - лак дизлайкнутого, дизлайк лайкнутого: как обработать?
            recipe = Recipe.objects.get(pk=recipe_id)
            status = ''
            if is_dislike:
                recipe.dislikes.add(telegram_id)
                status = f"{telegram_id} dislikes {recipe_id}"
            else:
                recipe.likes.add(telegram_id)
                status = f"{telegram_id} likes {recipe_id}"
            return {'status': status}
        except Recipe.DoesNotExist:
            raise ValidationError(f'Рецепт с ID {recipe_id} не найден.')
