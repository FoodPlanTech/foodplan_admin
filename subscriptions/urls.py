from django.urls import path

from .views import SubscriptionListViewSet, create_payment

urlpatterns = [
    path('payments/', create_payment, name='payments'),
    path('subscriptions/', SubscriptionListViewSet.as_view(), name='subscriptions'),
]
