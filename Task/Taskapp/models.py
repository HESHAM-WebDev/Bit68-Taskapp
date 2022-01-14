from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):

     email = models.EmailField(max_length=150, unique=True)
     password = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    seller = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.seller

    class Meta:
        ordering = ['price']