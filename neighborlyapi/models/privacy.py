"""Privacy Model Module"""
from django.db import models

class Privacy(models.Model):
    """
    Privacy class
    """
    label = models.CharField(max_length=25)
