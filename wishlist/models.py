from django.db import models

from user.models import User
from product.models import Product


class Wishlist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product)
