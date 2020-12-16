"""Privacy Model Module"""
from django.db import models

class Privacy(models.Model):
    """
    Privacy class

    Purpose: Create Privacy instances
    Associated Models:
    """
    label = models.CharField(max_length=25)
