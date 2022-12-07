from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=200)
    temprature = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    humidity = models.CharField(max_length=200)
    pressure = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    sunrise = models.CharField(max_length=200)
    sunset = models.CharField(max_length=200)
    windspeed = models.CharField(max_length=200)

class Test(models.Model):
    title= models.CharField(max_length=100)
    dec= models.CharField(max_length=100)

    