from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'guide',
            'image',
            'ingredients',
            'likes_count',
        )
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'liked_recipes',
        )
