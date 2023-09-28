import random

from django.db.models import Count
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import viewsets, views, status, generics

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
