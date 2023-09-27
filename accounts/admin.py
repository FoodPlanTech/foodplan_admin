from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from recipes.models import Recipe


class FavouriteRecipeInline(admin.TabularInline):
    model = Recipe.likes.through
    extra = 0
    raw_id_fields = ['recipe']

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "is_staff",
    ]
    inlines = [FavouriteRecipeInline]
    raw_id_fields = ('liked_recipes',)
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
