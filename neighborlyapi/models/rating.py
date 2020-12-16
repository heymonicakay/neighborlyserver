"""Rating Model Module"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Rating(models.Model):
    """
    Rating class

    Purpose: Create Rating instances
    Associated Models:
    """
    label = models.CharField(max_length=25)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
