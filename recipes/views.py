from rest_framework import viewsets

from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsStaffOrReadOnly


class RecipeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsStaffOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
