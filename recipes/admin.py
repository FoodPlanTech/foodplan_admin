from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredients


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredients
    extra = 3
    verbose_name = 'Ингредиент'
    verbose_name_plural = 'Состав рецепта'
    model.ingredient.field.verbose_name = 'Ингредиент'
    model.__str__ = lambda _: ''


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    raw_id_fields = ('likes',)
    inlines = [RecipeIngredientInline]
