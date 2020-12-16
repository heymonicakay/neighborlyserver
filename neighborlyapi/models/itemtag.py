"""Item Tag Model Module"""
from django.db import models

class ItemTag(models.Model):
    """Item Tag Model"""
    tag = models.ForeignKey(
        "Tag", on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="item_tags")
