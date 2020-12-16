"""Item Review Model Module"""
from django.db import models
from . import Reservation, Neighbor, Rating, DescriptionAccuracy, Item

class ItemReview(models.Model):
    """Item Review Model"""
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="reservations")
    author = models.ForeignKey(
        Neighbor, on_delete=models.CASCADE, related_name="written_reviews")
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="reviews")
    rating = models.ForeignKey(
        Rating, on_delete=models.DO_NOTHING)
    description_accuracy = models.ForeignKey(
        DescriptionAccuracy, on_delete=models.DO_NOTHING)
    created_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    details = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
