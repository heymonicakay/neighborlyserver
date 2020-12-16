"""ItemTag Model Module"""
from django.db import models
from . import Tag, Item

class ItemTag(models.Model):
    """ItemTag Model"""
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="item_tags")
