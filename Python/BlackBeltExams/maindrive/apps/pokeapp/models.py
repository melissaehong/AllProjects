from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

# Create your models here.
class PokeManager(models.Manager):
    def create_poke():
        pass


class Poke(models.Model):
    poke = models.IntegerField(default = 1)
    poker = models.ForeignKey(User, related_name = 'poker')
    pokee = models.ForeignKey(User, related_name = 'pokee')

    objects = PokeManager()
