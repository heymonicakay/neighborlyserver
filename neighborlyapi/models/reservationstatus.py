"""Reservation Status Model Module"""
from django.db import models

class ReservationStatus(models.Model):
    """R
    eservation Status class
    """
    label = models.CharField(max_length=25)
