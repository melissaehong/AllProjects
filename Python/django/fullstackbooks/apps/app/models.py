from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 45)
    category = models.CharField(max_length = 45)
    author = models.CharField(max_length = 45)
