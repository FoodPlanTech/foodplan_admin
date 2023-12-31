from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from djmoney.models.fields import MoneyField
from accounts.models import TelegramAccount
from subscriptions.models import Subscription


class Ingredient(models.Model):
    """
    Часть рецепта: овсяные хлопья, гречневая крупа, помидор и пр.
    """
    title = models.CharField('Ингредиент', max_length=200)
    price = MoneyField('Цена', max_digits=14, decimal_places=2,
                       default_currency='RUB')
    calories = models.IntegerField('Калорийность (ккал)', null=True,
                                   blank=True)

    def __str__(self):
        return self.title


class Preference(models.Model):
    title = models.CharField(max_length=128, blank=True)

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
        TelegramAccount,
        related_name='liked_recipes',
        verbose_name='Кто любит (ID пользователей)',
        blank=True)
    dislikes = models.ManyToManyField(
        TelegramAccount,
        related_name='disliked_recipes',
        verbose_name='Кто не любит (ID пользователей)',
        blank=True)
    is_teaser = models.BooleanField('Показывать в превью')
    preferences = models.ManyToManyField(Preference, related_name='recipes',
                                         verbose_name='Предпочтения')

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


class FoodPlan(models.Model):
    tg_account = models.OneToOneField(
        TelegramAccount,
        related_name='food_plan',
        verbose_name='Telegram ID',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    preferences = models.ManyToManyField(Preference, related_name='food_plans',
                                         verbose_name='Предпочтения')
    recipes_count = models.PositiveSmallIntegerField('Кол-во рецептов',
                                                     default=1, null=True, blank=True)
    subscription = models.ForeignKey(
        Subscription, related_name='food_plans', on_delete=models.CASCADE,
        verbose_name='Подписка',
        null=True, blank=True)
    start_date = models.DateField(
        'Начало', auto_now=True, null=True, blank=True)

    @property
    def end_date(self):
        verbose_name = 'Конец'
        if self.start_date:
            return self.start_date + self.subscription.duration

    def __str__(self):
        return f'{self.subscription}, {self.tg_account}, {self.start_date}—{self.end_date}'
