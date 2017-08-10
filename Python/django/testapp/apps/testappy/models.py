from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def login(self, email, password):
        print "Login!"
        return "Login method"
    def register(self, **kwargs):
        print "Register!"
        return "Register Method"

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
