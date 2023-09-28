from django.contrib import admin

from .models import Subscription, UserSubscription, Payment


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration', 'is_active')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'amount', 'user')
    list_filter = ['amount', 'user', 'created_at']


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'start_date', 'end_date', 'user')
