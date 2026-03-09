from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Order,OrderItem
from .serializers import OrderSerializers, OrderItemSerializer

class OrderViewSets(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializers
    permission_classes=[IsAuthenticated]

class OrderItemViewSets(viewsets.ModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class= OrderItemSerializer
    permission_classes=[IsAuthenticated]
    