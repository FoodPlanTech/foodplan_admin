from rest_framework import serializers

from .models import Recipe, FoodPlan


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
            'user',
            'preferences',
        )
        depth = 1
