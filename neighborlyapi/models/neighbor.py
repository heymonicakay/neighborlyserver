"""Neighbor Model Module"""
from django.db import models
from django.conf import settings

class Neighbor(models.Model):
    """Neighbor Model"""
    bio = models.CharField(max_length=500)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    streetOne = models.CharField(max_length=100)
    streetTwo = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=12)

    @property
    def username(self):
        """This makes the username property accessible directly from the Neighbor"""
        return self.user.username

    @property
    def admin(self):
        """This makes the is_staff property accessible directly from the Neighbor"""
        return self.user.is_staff

    @property
    def active(self):
        """This makes the is_active property accessible directly from the Neighbor"""
        return self.user.is_active

    @property
    def email(self):
        """This makes the email property accessible directly from the Neighbor"""
        return self.user.email

    @property
    def first_name(self):
        """This makes the email property accessible directly from the Neighbor"""
        return self.user.first_name

    @property
    def last_name(self):
        """This makes the email property accessible directly from the Neighbor"""
        return self.user.last_name

    @property
    def full_name(self):
        """This makes the first and last name
        properties accessible directly from the Neighbor
        as the full_name property"""
        return (f'{self.user.first_name} {self.user.last_name}')

    @property
    def joined_date(self):
        """This makes the date_joined property accessible directly from the Neighbor"""
        return self.user.date_joined

    @property
    def current_user(self):
        """This unmapped property has a boolean value"""
        return self.__current_user

    @current_user.setter
    def is_current_user(self, value):
        """This allows the is_current_user property to be set"""
        self.__current_user = value
