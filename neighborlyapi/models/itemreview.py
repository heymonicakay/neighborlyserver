"""Item Review Model Module"""
from django.db import models
from . import Reservation, Neighbor, ItemRating, DescriptionAccuracy, Item

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
        Item, on_delete=models.CASCADE, related_name="item_reviews")
    rating = models.ForeignKey(
        ItemRating, on_delete=models.DO_NOTHING)
    description_accuracy = models.ForeignKey(
        DescriptionAccuracy, on_delete=models.DO_NOTHING)
    created_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    details = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    @property
    def score(self):
        return self.rating.score
