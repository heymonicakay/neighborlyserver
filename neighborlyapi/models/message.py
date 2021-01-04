"""Message Model Module"""
from django.db import models
from .item import Item
from .reservation import Reservation
from .neighbor import Neighbor

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
    sent_date = models.DateTimeField(
        auto_now_add=True)
    read_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    body = models.TextField(max_length=2000)

    @property
    def read(self):
        """
        Property to set message read status based on whether or not the
        message has a 'read_date' property.

        Returns:
            Boolean -- Mesage has been read
        """
        read = self.read_date

        return read is not None
