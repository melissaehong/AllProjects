from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

class UserManager(models.Manager):
    def isValidRegistration(self, request):
        errors = []
        if len(request.POST['name']) < 2:
            errors.append('Name can not be less than 2 characters')

        if len(request.POST['alias']) < 2:
            errors.append('Alias can not be less than 2 characters')

        if len(request.POST['email']) < 1:
            errors.append('Email can not be empty')
        elif not EMAIL_REGEX.match(request.POST['email']):
            errors.append('Email is not valid')

        if len(request.POST['password']) < 1:
            errors.append('Password can not be empty')
        elif len(request.POST['password']) < 8:
            errors.append('Password should be more than 7 characters')
        elif not PASSWORD_REGEX.match(request.POST['password']):
            errors.append('Password should contain at least one upper case letter and one number')

        if request.POST['password'] != request.POST['confirm_password']:
            errors.append('Password and Confirm Password does not match!')

        try:
            user = User.objects.get(email = request.POST['email'])
            errors.append('This email is already being used')
        except ObjectDoesNotExist:
            pass

        if len(errors) > 0:
            return [False, errors]

        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = self.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=pw_hash, birthday=request.POST['birthday'])
        return [True, user]

    def isValidLogin(self, request):
        errors = []
        try:
            user = User.objects.get(email = request.POST['email'])
            password = user.password.encode()
            login_input_password = request.POST['password'].encode()
            print "*"*40
            print password
            print bcrypt.hashpw(login_input_password, password)
            print "*"*40
            if bcrypt.hashpw(login_input_password, password) == password:
                return (True, user)
            else:
                errors.append("Sorry, no password match")
                return (False, errors)
        except ObjectDoesNotExist:
            pass
        errors.append("Sorry, no email found. Please try again.")
        return (False, errors)



class PokeManager(models.Manager):
    def poking(self, from_user, to_user):
        try:
            poke = Poke.objects.get(from_user=from_user, to_user=to_user)
            poke.count += 1
            poke.save()
        except:
            fr_user = User.objects.get(id=from_user)
            t_user = User.objects.get(id=to_user)
            poke = Poke.objects.create(from_user=fr_user, to_user=t_user)
        return poke

    def get_poke_history(self, from_user, to_user):
        try:
            pokes = Poke.objects.all().filter(to_user=to_user)
            sum = 0
            for poke in pokes:
                sum += poke.poke_count
            return sum
        except:
            return 0

    def get_poked_history(self, id):
        try:
            pokes = Poke.objects.all().filter(to_user=id).order_by('-count')
            return pokes
        except:
            return {}

class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=225)
    birthday = models.DateField()

    objects = UserManager()

class Poke(models.Model):
    from_user = models.ForeignKey('User', null=True, related_name='from_user')
    to_user = models.ForeignKey('User', null=True, related_name='to_user')
    count = models.IntegerField(default=1)

    objects = PokeManager()
