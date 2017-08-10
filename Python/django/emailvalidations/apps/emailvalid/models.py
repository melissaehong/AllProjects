from __future__ import unicode_literals
from django.db import models
import re

emailregex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class EmailManager(models.Manager):
    def register(self, email):
        errors = []
        if len(email) == 0:
            errors.append('Email is required!')
        elif not emailregex.match(email):
            errors.append('Invalid Email')
        if len(errors) is not 0:
            return(False, errors)
        else:
            e = Email.objects.create(email=email)
            e.save()
            return(True, e)

    def destroy(self, id):
        e = Email.objects.get(id=id)
        if not e:
            return(False, 'No email found with that ID')
        else:
            e.delete()
            return(True, "Email deleted")

class Email(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = EmailManager()
