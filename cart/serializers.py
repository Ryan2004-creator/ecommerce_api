from rest_framework import serializers
from .models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['user', 'created_at']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=['cart', 'product', 'quantity']
