"""Description Accuracy Model Module"""
from django.db import models

class DescriptionAccuracy(models.Model):
    """Description Accuracy Model"""
    label = models.CharField(max_length=25)
