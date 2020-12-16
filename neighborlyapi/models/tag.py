"""Tag Model Module"""
from django.db import models

class Tag(models.Model):
    """
    Tag class

    Purpose: Create Tag instances
    Associated Models: 
    """
    label = models.CharField(max_length=50)
