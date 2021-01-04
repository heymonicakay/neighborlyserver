"""User Review Model Module"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .reservation import Reservation
from .type_of_user import TypeOfUser

class UserReview(models.Model):
    """
    User Review class

    Purpose: Create UserReview instances
    Associated Models: Neighbor
    """
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="reservations")
    reviewer = models.ForeignKey(
        "Neighbor", on_delete=models.CASCADE, related_name="users_reviewed")
    user = models.ForeignKey(
        "Neighbor", on_delete=models.CASCADE, related_name="user_reviews")
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    type_of_user = models.ForeignKey(
        TypeOfUser, on_delete=models.DO_NOTHING)
    created_date = models.DateField(
        auto_now_add=True)
    details = models.CharField(
        max_length=500)
    subject = models.CharField(
        max_length=50)
