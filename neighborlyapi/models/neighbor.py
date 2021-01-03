"""Neighbor Model Module"""
from django.db import models
from django.conf import settings

class Neighbor(models.Model):
    """
    Neighbor class

    Purpose: Create Neighbor instances
    Associated Models:
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    street_one = models.CharField(max_length=100)
    street_two = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=12)

    # @property
    # def reviews(self):
    #     """
    #     Property to access each users's associated userreview instances
    #     """
    #     try:
    #         reviews = UserReview.objects.filter(user=self)
    #         return reviews
    #     except UserReview.DoesNotExist:
    #         reviews = null
    #         return reviews

    # @property
    # def lender_review_count(self):
    #     """
    #     Property to set each users's lender review count

    #     Returns:
    #         Number -- The lender review count for the user
    #     """
    #     try:
    #         reviews = UserReview.objects.filter(user=self, user_type.id=2)
    #         total = len(reviews)
    #         return total
    #     except UserReview.DoesNotExist:
    #         total = 0
    #         return total

    # @property
    # def borrower_review_count(self):
    #     """
    #     Property to set each users's borrower review count

    #     Returns:
    #         Number -- The borrower review count for the user
    #     """
    #     try:
    #         reviews = UserReview.objects.filter(user=self, user_type.id=1)
    #         total = len(reviews)
    #         return total
    #     except UserReview.DoesNotExist:
    #         total = 0
    #         return total

    # @property
    # def avg_lender_rating(self):
    #     """
    #     Property to set each users's average lender rating

    #     Returns:
    #         Number -- The average lender rating for the user
    #     """
    #     try:
    #         reviews = UserReview.objects.filter(
    #             user=self, user_type.id=2)

    #         total = 0

    #         for r in reviews:
    #             total += r.score

    #         if total > 0:
    #             avg = total/ len(reviews)
    #             return avg
    #         else:
    #             avg = null
    #             return avg

    #     except ItemReview.DoesNotExist:
    #         avg = null
    #         return avg

    # @property
    # def avg_borrower_rating(self):
    #     """
    #     Property to set each users's average borrower rating

    #     Returns:
    #         Number -- The average borrower rating for the user
    #     """
    #     try:
    #         reviews = UserReview.objects.filter(
    #             user=self, user_type.id=1)

    #         total = 0

    #         for r in reviews:
    #             total += r.score

    #         if total > 0:
    #             avg = total/ len(reviews)
    #             return avg
    #         else:
    #             avg = null
    #             return avg

    #     except ItemReview.DoesNotExist:
    #         avg = null
    #         return avg

    @property
    def full_name(self):
        """This makes the first and last name
        properties accessible directly from the Neighbor
        as the full_name property"""
        return (f'{self.user.first_name} {self.user.last_name}')

    @property
    def current_user(self):
        """This unmapped property has a boolean value"""
        return self.__current_user

    @current_user.setter
    def current_user(self, value):
        """This allows the current_user property to be set"""
        self.__current_user = value
