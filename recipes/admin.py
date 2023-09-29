from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredients, Preference, FoodPlan


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredients
    extra = 3
    verbose_name = 'Ингредиент'
    verbose_name_plural = 'Состав рецепта'
    model.ingredient.field.verbose_name = 'Ингредиент'
    model.__str__ = lambda _: ''


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'list_preferences')
    raw_id_fields = ('likes', 'dislikes',)
    inlines = [RecipeIngredientInline]
    list_filter = ('preferences',)

    @admin.display(description='Предпочтения',)
    def list_preferences(self, obj):
        return ', '.join([t['title'] for t in obj.preferences.values('title')])


@admin.register(FoodPlan)
class FoodPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'list_preferences')
    list_filter = ('preferences', 'user')

    @admin.display(description='Предпочтения',)
    def list_preferences(self, obj):
        return ', '.join([t['title'] for t in obj.preferences.values('title')])
