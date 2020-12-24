"""ProfileImage Model Module"""
from django.db import models
from .neighbor import Neighbor


class ProfileImage(models.Model):
    """
    User Profile Image class

    Purpose: Create ProfileImage instances
    Associated Models:
    """
    image = models.ImageField(
        upload_to="profileimages/", blank=True, null=True)
    profile = models.ForeignKey(
        Neighbor, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
