from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price']
