"""Reservation Model Module"""
from django.db import models
from . import Item, ReservationStatus

class Reservation(models.Model):
    """
    Reservation class

    Purpose: Create Reservation instances
    Associated Models: 
    """
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="reservations")
    lender = models.ForeignKey(
        Neighbor, on_delete=models.CASCADE, related_name="reservations_received")
    borrower = models.ForeignKey(
        Neighbor, on_delete=models.CASCADE, related_name="reservations_sent")
    scheduled_start = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    scheduled_end = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    start = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.ForeignKey(
        ReservationStatus, on_delete=models.CASCADE)

    @property
    def messages(self):
        """
        Property to access each reservation's associated message instances

        message_set is a queryset of itemtags objects for which the reservation instance(aka self)'s primary key exists as that message's "reservation_id" foreign key
        """
        reservation_messages = self.message_set.all()
        return [reservation_messages]

    @property
    def returned(self):
        """Unmapped Prop"""
        return self.__returned

    @returned.setter
    def returned(self, value):
        """Unmapped Prop"""
        self.__returned = value
