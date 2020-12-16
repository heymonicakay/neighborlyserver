"""Item Review ImageModel Module"""
from django.db import models
from . import ItemReview

class ItemReviewImage (models.Model):
    """
    Item Review Image class

    Purpose: Create ItemReviewImage instances
    Associated Models:
    """
    item_review = models.ForeignKey(
        ItemReview, on_delete=models.CASCADE, related_name="images")
    image_url = models.ImageField(
        upload_to='itemreviewimages', height_field=None,
        width_field=None, max_length=None, null=True)
