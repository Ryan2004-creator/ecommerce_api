from django.db import models

class Products(models.Model):
    product_name=models.CharField(max_length=20)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()
    category=models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Category(models.Model):
    name=models.CharField(max_length=50)
    description= models.TextField()

    def __str__(self):
        return self.name
