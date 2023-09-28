from rest_framework.routers import SimpleRouter

from .views import SubscriptionViewSet


router = SimpleRouter()
router.register('subscriptions', SubscriptionViewSet, basename='subscriptions')

urlpatterns = router.urls
