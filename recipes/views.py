from rest_framework import viewsets, generics

from .models import Recipe, Preference, FoodPlan
from .serializers import RecipeSerializer, PreferenceSerializer, FoodPlanSerializer
from .permissions import IsStaffOrReadOnly


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
