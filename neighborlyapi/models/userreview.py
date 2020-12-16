"""User Review Model Module"""
from django.db import models

class UserReview(models.Model):
    """
    User Review class

    Purpose: Create Condition instances
    Associated Models: Neighbor
    """
    reservation = models.ForeignKey(
        "Reservation", on_delete=models.CASCADE, related_name="reservations")
    author = models.ForeignKey(
        "Neighbor", on_delete=models.CASCADE, related_name="written_reviews")
    user = models.ForeignKey(
        "Neighbor", on_delete=models.CASCADE, related_name="reviews")
    rating = models.ForeignKey(
        "Rating", on_delete=models.DO_NOTHING)
    responsiveness = models.ForeignKey(
        "Responsiveness", on_delete=models.DO_NOTHING)
    user_type = models.ForeignKey(
        "UserType", on_delete=models.DO_NOTHING)
    created_date = models.DateField(
        auto_now_add=True)
    details = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
