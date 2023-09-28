from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import RecipeViewSet, TeaserViewSet


router = SimpleRouter()
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('teasers', TeaserViewSet.as_view(), name='teasers'),
] + router.urls
