from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import RecipeViewSet, CurrentRecipeViewSet, UserViewSet


router = SimpleRouter()
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    # path("<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path('current-recipe', CurrentRecipeViewSet.as_view(), name="current_recipe"),
] + router.urls
