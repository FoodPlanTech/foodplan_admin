from django.urls import path

from .views import RecipeList, RecipeDetail

urlpatterns = [
    path("<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("", RecipeList.as_view(), name="recipe_list"),
]
