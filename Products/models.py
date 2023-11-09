from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.price}, {self.rating}"
