from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def registration(self, request):
        user = self.create(name = request.POST['name'])
        return user
    def validations(self, request):
        request.session['errors'] = []
        request.session['success'] = []
        if len(request.POST['name']) < 8:
            request.session['errors'].append('Error! Name too short')
            return request.session['errors']
        else:
            pass
    def userExists(self, request):
        try:
            User.objects.get(name = request.POST['name'])
            request.session['errors'].append('Username already exists!')
            return request.session['errors']
        except User.DoesNotExist:
            pass

class User(models.Model):
    name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()
