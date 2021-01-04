"""Item Review ImageModel Module"""
from django.db import models
from .item_review import ItemReview

class ItemReviewImage (models.Model):
    """
    Item Review Image class

    Purpose: Create ItemReviewImage instances
    Associated Models:
    """
    image = models.ImageField(
        upload_to='itemreviewimages/', blank=True, null=True)
    item_review = models.ForeignKey(
        ItemReview, on_delete=models.CASCADE, related_name="itemreviewimages", blank=True, null=True)
