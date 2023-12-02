#model for each chocolate entry

from django.db import models;


class Chocolate(models.Model):
    docno = models.CharField(max_length=255, unique=True)
    site = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    ingredients = models.JSONField(default=list)
    allergens = models.JSONField(default=list)
    price = models.CharField(max_length=20)


def __str__(self):
    return self.title