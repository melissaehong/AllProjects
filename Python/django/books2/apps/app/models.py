from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 45)
    author = models.CharField(max_length = 45)
    published_date = models.DateTimeField(default = 2006-10-25)
    category = models.CharField(max_length = 45)
    in_print = models.BooleanField(default = True)
    my_name = models.CharField(max_length = 45, default = 'Melissa')
