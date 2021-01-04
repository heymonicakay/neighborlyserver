"""User Type Model Module"""
from django.db import models

class TypeOfUser(models.Model):
    """
    TypeOfUser class

    Purpose: Create TypeOfUser instances
    Associated Models: TypeOfUser
    """
    label = models.CharField(max_length=25)
