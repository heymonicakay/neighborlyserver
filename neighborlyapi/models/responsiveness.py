"""Responsiveness Model Module"""
from django.db import models

class Responsiveness(models.Model):
    """
    Responsiveness class
    """
    label = models.CharField(max_length=25)
