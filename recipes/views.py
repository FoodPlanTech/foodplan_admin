from rest_framework import viewsets, generics

from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsStaffOrReadOnly


class RecipeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsStaffOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class TeaserViewSet(generics.ListAPIView):
    queryset = Recipe.objects.filter(is_teaser=True)
    serializer_class = RecipeSerializer
