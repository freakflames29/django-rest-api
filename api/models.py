from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=10)
    category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} > {self.price } > {self.category}"


