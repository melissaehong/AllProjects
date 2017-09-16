from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User
from datetime import datetime

# Create your models here.

class TripManager(models.Manager):
    def validate_review(self, post_data):
        errors = []
        today = datetime.now().date()
        start = datetime.strptime(post_data['start_date'], '%Y-%m-%d').date()
        end = datetime.strptime(post_data['end_date'], '%Y-%m-%d').date()

        if len(post_data['description']) < 1 or len(post_data['destination']) < 1:
            errors.append('fields are required')
        if start < today or end < today:
            errors.append(['date', 'Traveling dates must be in the future.'])
        # #validate date to not before date from
        if end < start:
            errors.append(['date', 'End date must be later than start date.'])

        return errors

    def create_trip(self, clean_data, user):
        newTrip = Trip.objects.create(
            destination = clean_data['destination'],
            description = clean_data['description'],
            start_date = clean_data['start_date'],
            end_date = clean_data['end_date'],
            planner = user
        )
        newTrip.travelers.add(user)
        newTrip.save()

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    planner = models.ForeignKey(User, related_name = 'trip_planner')
    travelers = models.ManyToManyField(User, related_name = 'trip_travelers')
    objects = TripManager()
