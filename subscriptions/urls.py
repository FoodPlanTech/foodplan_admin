from django.urls import path

from .views import SubscriptionListViewSet, CreatePaymentViewSet

urlpatterns = [
    path('payments/', CreatePaymentViewSet.as_view(), name='payments'),
    path('subscriptions/', SubscriptionListViewSet.as_view(), name='subscriptions'),
]
