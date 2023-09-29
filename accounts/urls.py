from rest_framework.routers import SimpleRouter

from .views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
# router.register('telegram_users', TelegramUserViewSet,
#                 basename='telegram_users')

urlpatterns = [
] + router.urls
