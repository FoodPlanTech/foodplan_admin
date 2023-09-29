from rest_framework.routers import SimpleRouter

from .views import UserViewSet, TelegramAccountViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('tg-accounts', TelegramAccountViewSet,
                basename='tg_accounts')

urlpatterns = [
] + router.urls
