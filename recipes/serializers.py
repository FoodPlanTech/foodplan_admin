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
    def create(self, validated_data):
        pref_ids = validated_data.pop('preference_ids')
        user_id = validated_data.pop('user_id')
        prefs = Preference.objects.filter(pk__in=pref_ids)
        print(pref_ids, user_id)
        fp = FoodPlan.objects.create(user_id=user_id) \
            .preferences.set(prefs)
        return fp

    class Meta:
        model = FoodPlan
        fields = (
            'user',
            'preferences',
        )
        depth = 1
