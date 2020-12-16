"""Message Status Model Module"""
from django.db import models

class MessageStatus(models.Model):
    """Message Status Model"""
    label = models.CharField(max_length=25)
