from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)

class Dish(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel')
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=100)