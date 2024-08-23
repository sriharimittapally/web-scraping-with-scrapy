from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=100)
    url = models.URLField()
    title = models.CharField(max_length=200)
    price = models.FloatField()
    mrp = models.FloatField()
    last_7_day_sale = models.FloatField()
    fit = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    neck = models.CharField(max_length=100)
    sleeve = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.title