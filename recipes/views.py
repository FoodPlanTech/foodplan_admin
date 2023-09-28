import random

from django.db.models import Count
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import viewsets, views, status, generics

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


class TeaserViewSet(generics.ListAPIView):
    queryset = Recipe.objects.filter(is_teaser=True)
    serializer_class = RecipeSerializer
