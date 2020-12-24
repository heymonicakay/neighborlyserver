"""Item Review Image Model Module"""
from django.db import models
from .itemreview import ItemReview

class ItemReviewImage(models.Model):
    """
    Item Review Image class

    Purpose: Create ReviewImage instances
    Associated Models:
    """
    image = models.ImageField(
        upload_to='itemreviewimages/', null=True, blank=True)
    item_review = models.ForeignKey(
        ItemReview, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
