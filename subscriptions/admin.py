from django.contrib import admin

from .models import Subscription, UserSubscription, Payment


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration', 'is_active')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'amount', 'tg_account')
    list_filter = ['amount', 'tg_account', 'created_at']
