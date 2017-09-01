from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

# Create your models here.

class TripManager(models.Manager):
    def validate_review(self, post_data):
        errors = []

        if len(post_data['description']) < 1 or len(post_data['destination']) < 1:
            errors.append('fields are required')

        return errors

    def create_trip(self, clean_data, name):
        self.create(
            destination = clean_data['destination'],
            description = clean_data['description'],
            start_date = clean_data['start_date'],
            end_date = clean_data['end_date'],
            trippers = name
        )

    def trip_and_trippers(self):
        '''
        returns a tuple with the zeroeth index containing query for 3 most recent reviews, and the first index
        containing the rest
        '''
        return (self.all().order_by('destination')[:3], self.all().order_by('destination')[3:])

class Trip(models.Model):
    user = models.ForeignKey(User, related_name = 'trips')

class Trip_Review(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    planner = models.ForeignKey(User, related_name = 'trip_planner')
    travelers = models.ManyToManyField(User, related_name = 'trip_travelers')
    objects = TripManager()
