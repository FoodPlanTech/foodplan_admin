from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Recipe, Preference
from .serializers import RecipeSerializer, PreferenceSerializer, GetRecipeQuerySerializer
from .permissions import IsStaffOrReadOnly


@api_view(['GET'])
def get_current_recipe(request):
    """Просмотр рекомендуемого рецепта пользователя в соответствии с предпочтениями."""
    serializer = GetRecipeQuerySerializer(data=request.query_params)

    if serializer.is_valid():
        recipe = serializer.create(serializer.data, request)
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
