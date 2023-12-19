from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    ID = models.CharField(max_length=255,null = True) 
    type = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='category_images/')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name 