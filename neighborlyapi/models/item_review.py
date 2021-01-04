"""Item Review Model Module"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .reservation import Reservation
from .neighbor import Neighbor
from .description_accuracy import DescriptionAccuracy

class ItemReview(models.Model):
    """
    Item Review class

    Purpose: Create ItemReview instances
    Associated Models: ItemReviewImage, Item
    """
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(
        Neighbor, on_delete=models.CASCADE, related_name="items_reviewed")
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="item_reviews")
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    description_accuracy = models.ForeignKey(
        DescriptionAccuracy, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(
        auto_now_add=True)
    details = models.CharField(
        max_length=500)
    subject = models.CharField(
        max_length=50)

    # @property
    # def score(self):
    #     return self.rating.score
