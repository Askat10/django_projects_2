from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField(max_length=4)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    

