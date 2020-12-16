"""Condition Model Module"""
from django.db import models

class Condition(models.Model):
    """
    Condition class

    Purpose: Create Condition instances
    Associated Models: Item
    """
    label = models.CharField(max_length=25)
