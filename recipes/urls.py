from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (PreferenceListViewSet, RecipeReadOnlyViewSet, TeaserListViewSet,
                    CurrentRecipeViewSet, CreateLikeViewSet, CreateDislikeViewSet)

router = SimpleRouter()
router.register('recipes', RecipeReadOnlyViewSet, basename='recipes')

urlpatterns = [
    path('teasers/', TeaserListViewSet.as_view(), name='teasers'),
    path('likes/', CreateLikeViewSet.as_view(), name='likes'),
    path('dislikes/', CreateDislikeViewSet.as_view(), name='dislikes'),
    path('preferences/', PreferenceListViewSet.as_view(), name='preferences'),
    path('current-recipe/', CurrentRecipeViewSet.as_view(), name='preferences'),
] + router.urls
