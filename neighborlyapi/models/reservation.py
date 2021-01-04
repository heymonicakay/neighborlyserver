"""Reservation Model Module"""
from django.db import models
from .reservation_status import ReservationStatus

class Reservation(models.Model):
    """
    Reservation class

    Purpose: Create Reservation instances
    Associated Models:
    """
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="reservations")
    user = models.ForeignKey(
        "Neighbor", on_delete=models.CASCADE, related_name="reservation_requests")
    requested_start = models.DateField(
        auto_now=False, auto_now_add=False)
    requested_end = models.DateField(
        auto_now=False, auto_now_add=False)
    start = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    end = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    res_status = models.ForeignKey(
        ReservationStatus, on_delete=models.CASCADE)

    @property
    def returned(self):
        """Unmapped Prop"""
        return self.__returned

    @returned.setter
    def returned(self, value):
        """Unmapped Prop"""
        self.__returned = value
