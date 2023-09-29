from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import SubscriptionViewSet, create_payment


router = SimpleRouter()
router.register('subscriptions', SubscriptionViewSet, basename='subscriptions')

urlpatterns = [
    path('payments', create_payment, name='payments'),
] + router.urls
