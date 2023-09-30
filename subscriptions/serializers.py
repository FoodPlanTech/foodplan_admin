from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import TelegramAccount
from recipes.models import FoodPlan, Preference

from .models import Payment, Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'id',
            'title',
            'price',
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'tg_account',
            'amount',
            'created_at',
        )


class CreatePaymentBodySerializer(serializers.Serializer):
    telegram_id = serializers.PrimaryKeyRelatedField(
        queryset=TelegramAccount.objects.all(), required=True)
    subscription_id = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.all(), required=True)
    preference_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Preference.objects.all()
    )

    def create(self, validated_data):
        subscription_id = validated_data.get('subscription_id')
        amount = Subscription.objects.get(pk=subscription_id).price

        telegram_id = validated_data.get('telegram_id')
        tg_account = TelegramAccount.objects.get(pk=telegram_id)

        preference_ids = validated_data.get('preference_ids')
        preferences = Preference.objects.filter(id__in=preference_ids)

        try:
            FoodPlan.objects.create(tg_account_id=telegram_id) \
                .preferences.set(preferences)
            payment = Payment.objects.create(
                tg_account=tg_account, amount=amount)
            return PaymentSerializer(payment).data

        except IntegrityError as error:
            raise ValidationError(
                f'FoodPlan для Telegram ID {telegram_id} уже существует.') from error
