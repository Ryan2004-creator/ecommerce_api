from rest_framework import serializers
from .models import Products, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['product_name', 'description', 'price', 'stock', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name', 'description']
