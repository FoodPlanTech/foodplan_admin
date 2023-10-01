from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Subscription
from .serializers import CreatePaymentBodySerializer, SubscriptionSerializer


class SubscriptionListViewSet(generics.ListAPIView):
    """Список вариантов подписок."""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


@api_view(['POST'])
def create_payment(request):
    """Зафиксировать платёж и создать фудплан для пользователя."""
    serializer = CreatePaymentBodySerializer(data=request.data)

    if serializer.is_valid():
        payment = serializer.create(serializer.data)
        return Response(payment, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
