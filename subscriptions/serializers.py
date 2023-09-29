from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from datetime import datetime

from rest_framework import serializers

from .models import Subscription, Payment
from accounts.models import TelegramAccount
from recipes.models import FoodPlan, Preference


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

        foodplan = FoodPlan.objects.create(tg_account_id=telegram_id) \
            .preferences.set(preferences)

        payment = Payment.objects.create(tg_account=tg_account, amount=amount)
        return PaymentSerializer(payment).data
