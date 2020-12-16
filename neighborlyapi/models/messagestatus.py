"""Message Status Model Module"""
from django.db import models

class MessageStatus(models.Model):
    """
    Message Status class

    Purpose: Create MessageStatus instances
    Associated Models: 
    """
    label = models.CharField(max_length=25)
