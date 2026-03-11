from django.contrib import admin
from .models import Products, Category

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'stock')
    search_fields = ('product_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
