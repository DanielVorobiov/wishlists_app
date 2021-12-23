from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=30)
    sku = models.CharField(max_length=15)
    price = models.FloatField()
    description = models.TextField(max_length=500)
