"""Item Model Module"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from . import Neighbor, Category, Condition, Privacy, ItemStatus

class Item(models.Model):
    """Item Model"""
    owner = models.ForeignKey(
        Neighbor, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=75)
    created_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    listed_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.CharField(max_length=255,)
    brand = models.CharField(max_length=255,)
    serial_number = models.CharField(max_length=100,)
    category = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default=1 related_name="items")
    condition = models.ForeignKey(
        Condition, on_delete=models.DO_NOTHING)
    privacy = models.ForeignKey(
        Privacy, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(
        ItemStatus, on_delete=models.DO_NOTHING)

    @property
    def tags(self):
        """
        Property to access each items's associated tag instances

        itemtag_set is a queryset of itemtags objects for which the item instance
        (aka self)'s primary key exists as that itemtag's "item_id" foreign key
        """

        item_tags = self.itemtag_set.all()
        return [item_tags]

    @property
    def reviews(self):
        """
        Property to access each items's associated itemreview instances

        itemreviews_set is a queryset of itemreview objects for which the item instance(aka self)'s primary key exists as that itemreview's "item_id" foreign key
        """

        reviews = self.item_reviews_set.all()
        return [reviews]

    @property
    def active(self):
        """Unmapped Prop"""
        return self.__active

    @active.setter
    def active(self, value):
        """Unmapped Prop"""
        self.__active = value

    @property
    def owner_full_name(self):
        """Unmapped Prop"""
        return self.owner.full_name

    @property
    def owner_username(self):
        """Unmapped Prop"""
        return self.owner.username

    @property
    def owner_is_active(self):
        """Unmapped Prop"""
        return self.owner.is_active
