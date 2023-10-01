from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (PreferenceListViewSet, RecipeReadOnlyViewSet, TeaserListViewSet,
                    get_current_recipe)

router = SimpleRouter()
router.register('recipes', RecipeReadOnlyViewSet, basename='recipes')

urlpatterns = [
    path('teasers/', TeaserListViewSet.as_view(), name='teasers'),
    path('preferences/', PreferenceListViewSet.as_view(), name='preferences'),
    path('current-recipe/', get_current_recipe, name='preferences'),
] + router.urls
