from rest_framework import serializers
from .models import Order, OrderItem

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['user', 'total_price', 'status', 'created_at']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=['order', 'product', 'price', 'quantity']

