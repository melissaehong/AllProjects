from __future__ import unicode_literals

from django.db import models
import re

email_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def validateRegister(self,request):
        errors = self.validate(request)

        if len(errors) > 0:
            return (False, errors)

        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'])

        return (True, user)

    def validateLogin(self, request):
        try:
            user = User.objects.get(email = request.POST['email'])
            password = User.objects.get(password = request.POST['password'])
            return (True, user)
        except User.DoesNotExist:
            pass

        return (False, ["Email/password don't match."])

    def validate(self, request):
        errors = []
        request.session['success'] = []
        if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
            errors.append('First/Last Name not long enough!')
        if request.POST['password'] != request.POST['confirm_password']:
            errors.append("Passwords don't match!")
        if len(request.POST['password']) < 8:
            errors.append("Password is too short!")
        if not email_REGEX.match(request.POST['email']):
            errors.append('Invalid Email')
        if len(request.POST['email']) < 2:
            errors.append('Email not long enough!')
        try:
            User.objects.get(email = request.POST['email'])
            errors.append('Username already exists!')
        except User.DoesNotExist:
            pass
        print errors
        return errors


    def login(self, request):
        pass

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    objects = UserManager()
