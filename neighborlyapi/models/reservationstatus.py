"""Reservation Status Model Module"""
from django.db import models

class ReservationStatus(models.Model):
    """
    Reservation Status class

    Purpose: Create ReservationStatus instances
    Associated Models: 
    """
    label = models.CharField(max_length=25)
