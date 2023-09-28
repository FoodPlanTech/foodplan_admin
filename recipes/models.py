from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from djmoney.models.fields import MoneyField


class Ingredient(models.Model):
    """
    Часть рецепта: овсяные хлопья, гречневая крупа, помидор и пр.
    """
    title = models.CharField('Ингредиент', max_length=200)
    price = MoneyField('Цена', max_digits=14, decimal_places=2,
                       default_currency='RUB')
    calories = models.IntegerField(
        'Калорийность (ккал)', null=True, blank=True)
    # TODO:
    # - подходит ли вегетерианцам?
    # - тут должна быть единица измерения?

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """
    Рецепт блюда: борщ, торт «Наполеон», овсянка с молоком и пр.
    """
    title = models.CharField('Название', max_length=200)
    image = models.ImageField(upload_to='recipes', null=True, blank=True,
                              verbose_name='Фото блюда')
    ingredients = models.ManyToManyField(
        Ingredient, through='RecipeIngredients',
    )
    guide = models.TextField('Инструкция', blank=True)
    likes = models.ManyToManyField(
        get_user_model(),
        related_name='liked_recipes',
        verbose_name='Кто любит (ID пользователей)',
        blank=True)
    dislikes = models.ManyToManyField(
        get_user_model(),
        related_name='disliked_recipes',
        verbose_name='Кто не любит (ID пользователей)',
        blank=True)
    is_teaser = models.BooleanField('Показывать в превью')

    def __str__(self):
        return self.title


class RecipeIngredients(models.Model):
    """
    Модель (вспомогательная) для связки ингредиентов с рецептами.
    """
    class Units(models.TextChoices):
        GRAMS = "GRAMS", _("Грамм")
        PIECES = "PIECES", _("Штук")
        LITERS = "LITERS", _("Литров")

    ingredient = models.ForeignKey(Ingredient, related_name='ingredients',
                                   on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='recipes',
                               on_delete=models.CASCADE)
    amount = models.IntegerField('Вес/Объём/Кол-во')
    units = models.CharField('Ед. измерения', max_length=56, choices=Units.choices,
                             default=Units.GRAMS)
