import random

from django.db.models import Count
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import viewsets, views, status

from .models import Recipe
from .serializers import RecipeSerializer, UserSerializer
from .permissions import IsStaffOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsStaffOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CurrentRecipeViewSet(views.APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        rand_recipe = random.choice(list(recipes))
        serializer = RecipeSerializer(rand_recipe)
        return Response(serializer.data)
