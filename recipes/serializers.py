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


class GetRecipeQuerySerializer(serializers.Serializer):
    telegram_id = serializers.PrimaryKeyRelatedField(
        queryset=TelegramAccount.objects.all(), required=True)

    def retrieve(self, validated_data, request):
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
