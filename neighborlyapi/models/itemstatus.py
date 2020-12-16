"""Item Status Model Module"""
from django.db import models

class ItemStatus(models.Model):
    """Item Status Model"""
    label = models.CharField(max_length=25)
