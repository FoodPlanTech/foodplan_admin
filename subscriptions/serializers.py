from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import TelegramAccount
from recipes.models import FoodPlan, Preference

from .models import Payment, Subscription


class MoneySerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()


class SubscriptionSerializer(serializers.ModelSerializer):
    price = MoneySerializer()

    class Meta:
        model = Subscription
        fields = (
            'id',
            'title',
            'price',
        )


class FoodPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPlan
        fields = ('__all__')


class CreatePaymentBodySerializer(serializers.Serializer):
    telegram_id = serializers.PrimaryKeyRelatedField(
        queryset=TelegramAccount.objects.all(),
        required=True)
    subscription_id = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.all(),
        required=True)
    # TODO: тут почему-то валидация не работает, делается ниже в `create`
    preference_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Preference.objects.all(),
        required=True)

    def create(self, validated_data):
        subscription_id = validated_data.get('subscription_id')
        amount = Subscription.objects.get(pk=subscription_id).price

        telegram_id = validated_data.get('telegram_id')
        tg_account = TelegramAccount.objects.get(pk=telegram_id)

        preference_ids = validated_data.get('preference_ids')
        if not preference_ids:
            raise ValidationError(f'Укажите preference_ids.')
        preferences = Preference.objects.filter(id__in=preference_ids)

        try:
            Payment.objects.create(
                tg_account=tg_account, amount=amount)
            foodplan = FoodPlan.objects.create(tg_account_id=telegram_id)
            foodplan.preferences.set(preferences)
            return FoodPlanSerializer(foodplan).data

        except IntegrityError as error:
            raise ValidationError(
                f'FoodPlan для Telegram ID {telegram_id} уже существует.') from error
