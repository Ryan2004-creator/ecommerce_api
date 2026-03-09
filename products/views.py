from django.shortcuts import render
from  rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductViewSets(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer

class CategoryViewSets(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
