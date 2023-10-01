from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (PreferenceListViewSet, RecipeReadOnlyViewSet, TeaserListViewSet,
                    CurrentRecipeViewSet)

router = SimpleRouter()
router.register('recipes', RecipeReadOnlyViewSet, basename='recipes')

urlpatterns = [
    path('teasers/', TeaserListViewSet.as_view(), name='teasers'),
    path('preferences/', PreferenceListViewSet.as_view(), name='preferences'),
    path('current-recipe/', CurrentRecipeViewSet.as_view({'get': 'retrieve'}), name='preferences'),
] + router.urls
