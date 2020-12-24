"""Item Image Model Module"""
from django.db import models
from .item import Item

class ItemImage(models.Model):
    """
    ItemImage Model

    Purpose: Create ItemImage instances
    Associated Models:
    """
    image_url = models.ImageField(
        upload_to='itemimages', height_field=None,
        width_field=None, max_length=None, null=True)
    item = models.ForeignKey(
        Item, on_delete=models.DO_NOTHING, related_name="item_images")
