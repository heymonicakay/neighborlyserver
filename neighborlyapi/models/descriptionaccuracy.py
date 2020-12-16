"""Description Accuracy Model Module"""
from django.db import models

class DescriptionAccuracy(models.Model):
    """
    Description Accuracy class

    Purpose: Create DescriptionAccuracy instances
    Associated Models: ItemReview
    """
    label = models.CharField(max_length=25)
