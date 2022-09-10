from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
        
     
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
        
     
    def __str__(self):
        return self.name
    

class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    
    # Foreign keys:
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # "on_delete=models.SET_NULL" significa que aunque se elimine el usuario, no se elimina lo que él creó (ej. los productos)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    # Own attributes:
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    # Many to Many Fields:
    brand = models.ManyToManyField(Brand) 
    
     
    def __str__(self):
        return self.name




























