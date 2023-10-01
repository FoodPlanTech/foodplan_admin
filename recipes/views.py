from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from .models import Preference, Recipe
from .permissions import IsStaffOrReadOnly
from .serializers import (GetRecipeQuerySerializer, PreferenceSerializer,
                          RecipeSerializer, CreateLikeSerializer)


class CurrentRecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='telegram_id',
                description='Telegram ID пользователя',
                required=True,
                type=int),
        ]
    )
    def retrieve(self, request):
        """Просмотр рекомендуемого рецепта пользователя в соответствии с предпочтениями."""
        # return self.list(request, *args, **kwargs)
        serializer = GetRecipeQuerySerializer(data=request.query_params)

        if serializer.is_valid():
            recipe = serializer.retrieve(serializer.data, request)
            return Response(recipe, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
