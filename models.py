from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,  
 decimal_places=2)
    image = models.ImageField(upload_to='products/')  

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)  


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  

    created_at = models.DateTimeField(auto_now_add=True)  


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
