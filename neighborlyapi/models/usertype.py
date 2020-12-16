"""User Type Model Module"""
from django.db import models

class UserType(models.Model):
    """User Type Model"""
    label = models.CharField(max_length=25)
