from django.db import models
from django.contrib.auth.models import User
from products.models import Products

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
       return f"{self.user.username} - {self.product.product_name}"


