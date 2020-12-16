"""Category Model Module"""
from django.db import models

class Category(models.Model):
    """
    Category class

    Purpose: Create Category instances
    Associated Models: Item
    """
    label = models.CharField(max_length=50)
