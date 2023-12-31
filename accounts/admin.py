from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from recipes.models import Recipe

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, TelegramAccount


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


class TelegramAccountInline(admin.TabularInline):
    model = TelegramAccount


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "telegram",
        "is_staff",
    ]
    inlines = [TelegramAccountInline]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


@admin.register(TelegramAccount)
class TelegramAccountAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'created_at', 'user')
    inlines = [LikedRecipeInline, DislikedRecipeInline]
    raw_id_fields = ('liked_recipes', 'disliked_recipes',)
