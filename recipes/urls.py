from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import RecipeViewSet, TeaserViewSet, UserViewSet


router = SimpleRouter()
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('teasers', TeaserViewSet.as_view(), name='teasers'),
] + router.urls
