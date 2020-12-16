"""Condition Model Module"""
from django.db import models

class Condition(models.Model):
    """Condition Model"""
    label = models.CharField(max_length=25)
