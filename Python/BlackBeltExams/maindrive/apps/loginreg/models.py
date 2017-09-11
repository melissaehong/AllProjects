from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

email_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def validateRegister(self,request):
        errors = self.validate(request)

        if len(errors) > 0:
            return (False, errors)

        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(5))
        user = User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = pw_hash, birthdate = request.POST['birthdate'])

        return (True, user)

    def validateLogin(self, request):
        try:
            user = User.objects.get(email = request.POST['email'])
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.password.encode()) == user.password.encode():
                return (True, user)
        except User.DoesNotExist:
            pass

        return (False, ["Email/password don't match."])

    def validate(self, request):
        errors = []
        request.session['success'] = []
        if len(request.POST['name']) < 2 or len(request.POST['alias']) < 2:
            errors.append('Name/Alias not long enough!')
        if request.POST['password'] != request.POST['confirm_password']:
            errors.append("Passwords don't match!")
        if len(request.POST['password']) < 8:
            errors.append("Password is too short!")
        if len(request.POST['email']) < 2:
            errors.append('Email not long enough!')
        if not email_REGEX.match(request.POST['email']):
            errors.append('Invalid Email')
        try:
            User.objects.get(email = request.POST['email'])
            errors.append('Email already exists!')
        except User.DoesNotExist:
            pass
        print errors
        return errors

    def login(self, request):
        pass

class User(models.Model):
    name = models.CharField(max_length = 100)
    alias = models.CharField(max_length = 100)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    birthdate = models.DateTimeField()
    objects = UserManager()
    def __str__(self):
        return self.email
