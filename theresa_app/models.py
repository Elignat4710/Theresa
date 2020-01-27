from django.db import models


class Product(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=300)
    price = models.CharField(max_length=111)
    images = models.TextField()
    sizes = models.CharField(max_length=111)
    description = models.TextField()
    category = models.CharField(max_length=111)
    