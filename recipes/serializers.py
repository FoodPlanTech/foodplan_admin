from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Recipe, FoodPlan, Preference


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'guide',
            'image',
            'ingredients',
            'preferences',
        )
        depth = 1


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
        )


class FoodPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPlan
        fields = (
            'tg_account',
            'preferences',
        )
        depth = 1
