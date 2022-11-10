from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    owner = models.ForeignKey(
        User, related_name="orders", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="orders", on_delete=models.PROTECT)
