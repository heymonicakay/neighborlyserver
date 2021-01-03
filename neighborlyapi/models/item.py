"""Item Model Module"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .neighbor import Neighbor
from .category import Category
from .condition import Condition
from .itemreview import ItemReview


class Item(models.Model):
    """
    Item class

    Purpose: Create Item instances
    Associated Models: ItemImage, ItemReview, ItemTag
    """
    owner = models.ForeignKey(
        Neighbor, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(
        max_length=75)
    description = models.CharField(
        max_length=500)
    created_date = models.DateField(
        auto_now_add=True)
    listed_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    brand = models.CharField(
        max_length=255, null=True, blank=True)
    serial_number = models.CharField(
        max_length=100, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default=1, related_name="cat_items")
    condition = models.ForeignKey(
        Condition, on_delete=models.DO_NOTHING, related_name="cond_items")

    # TODO: Add Unmapped Privacy Prop
    # TODO: Add Unmapped item status Prop

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
    def draft(self):
        """
        Property to set item draft mode based on whether or not the item has a 'listed_date' property.

        Returns:
            Boolean -- Item in draft mode
        """
        listed = self.listed_date

        if listed is None:
            return True
        else:
            return False

    @property
    def average_rating(self):
        """
        Property to set each item's average rating

        Returns:
            Number -- The average rating for the item
        """
        try:
            reviews = ItemReview.objects.filter(
                item=self)

            total = 0

            for r in reviews:
                total += r.score

            if total > 0:
                avg = total/ len(reviews)
                return avg
            else:
                avg = null
                return avg

        except ItemReview.DoesNotExist:
            avg = null
            return avg

    @property
    def review_count(self):
        try:
            reviews = ItemReview.objects.filter(item=self)
            total = len(reviews)
            return total
        except ItemReview.DoesNotExist:
            total = 0
            return total

    @property
    def owner_full_name(self):
        """Unmapped Prop"""
        return self.owner.full_name

    @property
    def owner_username(self):
        """Unmapped Prop"""
        return self.owner.user.username

    @property
    def owner_is_active(self):
        """Unmapped Prop"""
        return self.owner.user.is_active
