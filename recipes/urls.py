from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import RecipeViewSet, TeaserViewSet, PreferenceViewSet, FoodPlanViewSet


router = SimpleRouter()
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('foodplans', FoodPlanViewSet, basename='foodplans')

urlpatterns = [
    path('teasers/', TeaserViewSet.as_view(), name='teasers'),
    path('preferences/', PreferenceViewSet.as_view(), name='preferences'),
] + router.urls
