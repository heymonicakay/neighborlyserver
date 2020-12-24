"""Item Tag Model Module"""
from django.db import models
from .tag import Tag
from .item import Item

class ItemTag(models.Model):
    """
    Item Tag class

    Purpose: Create ItemTag instances
    Associated Models:
    """
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="itemtags")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemtags")
