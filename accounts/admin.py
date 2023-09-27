from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from recipes.models import Recipe


class LikedRecipeInline(admin.TabularInline):
    model = Recipe.likes.through
    extra = 0
    raw_id_fields = ['recipe']
    verbose_name = 'Любимый рецепт'
    verbose_name_plural = 'Любимые рецепты'
    model.recipe.field.verbose_name = 'ID рецепта'
    model.__str__ = lambda _: 'любимый рецепт'


class DislikedRecipeInline(admin.TabularInline):
    model = Recipe.dislikes.through
    extra = 0
    raw_id_fields = ['recipe']
    verbose_name = 'Нелюбимый рецепт'
    verbose_name_plural = 'Нелюбимые рецепты'
    model.recipe.field.verbose_name = 'ID рецепта'
    model.__str__ = lambda _: 'нелюбимый рецепт'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "is_staff",
    ]
    inlines = [LikedRecipeInline, DislikedRecipeInline]
    raw_id_fields = ('liked_recipes', 'disliked_recipes',)
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
