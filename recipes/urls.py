from rest_framework.routers import SimpleRouter

from .views import RecipeViewSet

# urlpatterns = [
#     path("<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
#     path("", RecipeList.as_view(), name="recipe_list"),
# ]


router = SimpleRouter()
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = router.urls
