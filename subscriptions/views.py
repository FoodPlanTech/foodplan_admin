import random
from rest_framework.decorators import api_view


from django.db.models import Count
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import viewsets, views, status, generics

from .models import Subscription, Payment
from .serializers import SubscriptionSerializer, PaymentSerializer, \
    CreatePaymentBodySerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


@api_view(['POST'])
def create_payment(request):
    serializer = CreatePaymentBodySerializer(data=request.data)

    if serializer.is_valid():
        payment = serializer.create(serializer.data)
        return Response(payment, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
