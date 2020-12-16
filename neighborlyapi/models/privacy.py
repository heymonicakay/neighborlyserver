"""Privacy Model Module"""
from django.db import models

class Privacy(models.Model):
    """Privacy Model"""
    label = models.CharField(max_length=25)
