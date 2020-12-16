"""Item Model Module"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from . import Neighbor, Category, Condition, Privacy, ItemStatus, ItemReview

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
        max_length=255)
    serial_number = models.CharField(
        max_length=100)
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
    def draft(self):
        """
        Property to set item draft mode based on whether or not the item has a 'listed_date' property.

        Returns:
            Boolean -- Item in draft mode
        """
        listed = self.listed_date

        if listed is not None:
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
        return self.owner.username

    @property
    def owner_is_active(self):
        """Unmapped Prop"""
        return self.owner.is_active
