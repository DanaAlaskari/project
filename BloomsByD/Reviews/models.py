from django.db import models
from Catogries.models import Category

class Review(models.Model):
    flower = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255)
    opinion = models.TextField()


    def __str__(self):
        return self.username