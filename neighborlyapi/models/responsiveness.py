"""Responsiveness Model Module"""
from django.db import models

class Responsiveness(models.Model):
    """Responsiveness Model"""
    label = models.CharField(max_length=25)
