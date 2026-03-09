from django.db import models
from django.contrib.auth.models import User
from products.models import Products
#Cart
#user → foreign key to User
#created_at
#CartItem
#cart → foreign key to Cart
#product → foreign key to Product
#quantity

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)#only for one to one things
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return f"Cart {self.id} by {self.user.username}"
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self):
     return f"{self.product.product_name} in Cart {self.cart.id}"