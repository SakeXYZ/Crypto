from django.db import models


# Create your models here.
class Currency(models.Model):
    exchange = models.CharField(max_length=100)
    name = models.CharField(max_length=120)
    price = models.FloatField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
