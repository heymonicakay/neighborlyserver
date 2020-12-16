"""User Type Model Module"""
from django.db import models

class UserType(models.Model):
    """
    User Type class

    Purpose: Create UserType instances
    Associated Models: UserReview
    """
    label = models.CharField(max_length=25)
