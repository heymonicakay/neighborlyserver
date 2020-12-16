"""Rating Model Module"""
from django.db import models

class Rating(models.Model):
    """Rating Model"""
    label = models.CharField(max_length=25)
