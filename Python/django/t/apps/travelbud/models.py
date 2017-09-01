from __future__ import unicode_literals
from ..loginreg.models import User
from django.db import models

# Create your models here.

class TripManager(models.Manager):
    def validate_review(self, post_data):
        errors = []

        if len(post_data['description']) < 1 or len(post_data['destination']) < 1:
            errors.append('fields are required')

        return errors

    def create_review(self, clean_data, user_id):
        self.create(
            destination = clean_data['destination'],
            description = clean_data['description'],
            start_date = clean_date['start_date'],
            end_date = clean_data['end_date'],
            trippers = User.objects.get(id=user_id)
        )

    def trip_and_trippers(self):
        '''
        returns a tuple with the zeroeth index containing query for 3 most recent reviews, and the first index
        containing the rest
        '''
        return (self.all().order_by('destination')[:3], self.all().order_by('destination')[3:])


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    trippers = models.ManyToManyField(User, related_name = 'trips')
    objects = TripManager()
