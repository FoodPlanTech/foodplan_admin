from rest_framework import generics, status
from rest_framework.response import Response

from .models import Subscription, Payment
from .serializers import CreatePaymentBodySerializer, SubscriptionSerializer


class SubscriptionListViewSet(generics.ListAPIView):
    """Список вариантов подписок."""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class CreatePaymentViewSet(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = CreatePaymentBodySerializer

    def create(self, request):
        """Зафиксировать платёж и создать фудплан для пользователя."""
        serializer = CreatePaymentBodySerializer(data=request.data)

        if serializer.is_valid():
            foodplan = serializer.create(serializer.data)
            return Response(foodplan, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
