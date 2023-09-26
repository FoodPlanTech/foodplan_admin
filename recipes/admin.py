from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredients


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredients
    extra = 3
    verbose_name = 'Ингредиент'
    verbose_name_plural = 'Ингредиенты'
    model.ingredient.field.verbose_name = 'Ингредиент'
    model.__str__ = lambda _: 'Идентификатор ингредиента'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [RecipeIngredientInline]
