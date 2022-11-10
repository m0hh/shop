from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.


class Cart(models.Model):
    owner = models.OneToOneField(
        User, related_name='cart', on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product, related_name='carts', blank=True)
