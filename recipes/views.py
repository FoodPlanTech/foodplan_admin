import random
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, ParseError

from .models import Preference, Recipe, FoodPlan
from .permissions import IsStaffOrReadOnly
from .serializers import (PreferenceSerializer,
                          RecipeSerializer, CreateLikeSerializer)


class CurrentRecipeViewSet(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        resp = Recipe.objects.all()  # should always return queryset

        telegram_id = self.request.query_params.get('telegram_id')
        if not telegram_id:
            raise ParseError("Не найдет GEt-параметр telegram_id.")

        foodplan_qs = FoodPlan.objects.filter(pk=telegram_id) \
            .prefetch_related('preferences')
        if not foodplan_qs:
            raise ValidationError(
                f'FoodPlan для пользователя {telegram_id} не найден.')

        foodplan = foodplan_qs[0]
        preferences = foodplan.preferences.all()
        if not preferences:
            raise ValidationError(
                f'Предпочтения пользователя {telegram_id} не заполнены.')

        preferred_recipes = Recipe.objects.filter(preferences__in=preferences)
        preferred_ids = preferred_recipes.values_list(
            'pk').values_list('id', flat=True)
        qty = foodplan.recipes_count or 1
        random_recipe_ids = random.sample(list(preferred_ids), qty)
        resp = preferred_recipes.filter(pk__in=random_recipe_ids)
        return resp


class RecipeReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """Рецепты. Только просмотр, добавляются и редактируются через админку."""
    # permission_classes = (IsStaffOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class TeaserListViewSet(generics.ListAPIView):
    """Список демонстрационных рецептов, показываются бесплатно."""
    queryset = Recipe.objects.filter(is_teaser=True)
    serializer_class = RecipeSerializer


class PreferenceListViewSet(generics.ListAPIView):
    """Список возможных предпочтений в рационе."""
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer


class CreateLikeViewSet(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = CreateLikeSerializer

    def create(self, request):
        """Зафиксировать платёж и создать фудплан для пользователя."""
        serializer = CreateLikeSerializer(data=request.data)

        if serializer.is_valid():
            recipe = serializer.update(serializer.data)
            return Response(recipe, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDislikeViewSet(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = CreateLikeSerializer

    def create(self, request):
        """Зафиксировать платёж и создать фудплан для пользователя."""
        serializer = CreateLikeSerializer(data=request.data)

        if serializer.is_valid():
            recipe = serializer.update(serializer.data, is_dislike=True)
            return Response(recipe, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
