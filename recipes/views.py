from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Recipe, Preference, FoodPlan
from .serializers import RecipeSerializer, PreferenceSerializer, FoodPlanSerializer, GetRecipeQuerySerializer
from .permissions import IsStaffOrReadOnly


@api_view(['GET'])
def get_current_recipe(request):
    serializer = GetRecipeQuerySerializer(data=request.query_params)

    if serializer.is_valid():
        recipe = serializer.create(serializer.data)
        return Response(recipe, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsStaffOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class FoodPlanViewSet(viewsets.ModelViewSet):
    queryset = FoodPlan.objects.all()
    serializer_class = FoodPlanSerializer


class TeaserViewSet(generics.ListAPIView):
    queryset = Recipe.objects.filter(is_teaser=True)
    serializer_class = RecipeSerializer


class PreferenceViewSet(generics.ListAPIView):
    queryset = Preference.objects.filter()
    serializer_class = PreferenceSerializer
