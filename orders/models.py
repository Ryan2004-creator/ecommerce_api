from django.db import models
from django.contrib.auth.models import User
from products.models import Products
#3️ Orders App
#Order
#user → foreign key to User
#total_price
#status → Pending / Paid / Shipped / Delivered
#created_at
#OrderItem
#order → foreign key to Order
#product → foreign key to Product
#quantity
#price
class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    quantity=models.IntegerField()
    
    def __str__(self):
        return f"{self.product.product_name} (Order {self.order.id})"


    
