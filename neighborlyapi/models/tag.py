"""Tag Model Module"""
from django.db import models

class Tag(models.Model):
    """
    Tag class
    """
    label = models.CharField(max_length=50)
