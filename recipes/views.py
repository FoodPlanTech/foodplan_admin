import random

from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework import views
from rest_framework.generics import get_object_or_404

from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsStaffOrReadOnly


class RecipeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsStaffOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CurrentRecipeViewSet(views.APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        rand_recipe = random.choice(list(recipes))
        serializer = RecipeSerializer(rand_recipe)
        return Response(serializer.data)


# def current_meal(request):
#     """
#     Выдаёт актуальное блюдо из меню в зависимости от времени и дня недели.

#     Например, сейчас вторник, 13:00. Пользователь хочет поесть. Спрашивает бота.
#     Бот дёргает этот урл и получает блюдо из меню для текущей недели, которое соответствует
#     обеденному времени.

#     TODO: сейчас тупо рандомное выдается.
#     """
#     # rand_recipe = random.choice(list(recipes))
#     # serializer_class = RecipeSerializer
#     recipe = Recipe.objects.get(pk=1)
#     print(recipe)
#     return get_object_or_404(recipe)
