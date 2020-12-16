"""Item Review Image Model Module"""
from django.db import models
from . import Item

class ItemReviewImage(models.Model):
    """Item Review Image Model"""
    image_url = models.ImageField(
        upload_to='itemreviewimages', height_field=None,
        width_field=None, max_length=None, null=True)
    item_review = models.ForeignKey(
        ItemReview, on_delete=models.DO_NOTHING, related_name="item_review_images")
