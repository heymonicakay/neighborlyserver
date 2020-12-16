"""Message Model Module"""
from django.db import models
from . import Item, MessageStatus

class Message(models.Model):
    """
    Message class

    Purpose: Create Message instances
    Associated Models: 
    """
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(
        Neighbor, on_delete=models.DO_NOTHING, related_name="sent_messages")
    recipient = models.ForeignKey(
        Neighbor, on_delete=models.DO_NOTHING, related_name="received_messages")
    status = models.ForeignKey(
        MessageStatus, on_delete=models.DO_NOTHING)
    sent_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    read_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    @property
    def returned(self):
        """Unmapped Prop"""
        return self.__returned

    @returned.setter
    def returned(self, value):
        """Unmapped Prop"""
        self.__returned = value
