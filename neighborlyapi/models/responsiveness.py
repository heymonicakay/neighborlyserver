"""Responsiveness Model Module"""
from django.db import models

class Responsiveness(models.Model):
    """
    Responsiveness class

    Purpose: Create Responsiveness instances
    Associated Models: 
    """
    label = models.CharField(max_length=25)
