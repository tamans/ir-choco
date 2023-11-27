#model for each chocolate entry

from django.db import models;


class Chocolate(models.Model):
    docno = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    ingredients = models.JSONField(default=list)
    price = models.CharField(max_length=20)


def __str__(self):
    return self.name