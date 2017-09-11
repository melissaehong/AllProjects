from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

# Create your models here.
class PokeManager(models.Manager):
    def create_poke(self, poker_id, pokee_id):
        poker = User.objects.get(id=poker_id)
        pokee = User.objects.get(id=pokee_id)
        newPoke = Poke.objects.create(poker=poker, pokee=pokee)
        pokes = Poke.objects.filter(poker=poker, pokee=pokee)
        for poke in pokes:
            poke.poke_count += 1
            poke.save()
        print poker
        print pokee

    def get_poked_list(self, id):
        try:
            pokes = Poke.objects.all().filter(pokee=id).order_by('-poke_count')
            return pokes
        except:
            return {}

    def get_poke_list(self, poker, pokee):
        try:
            pokes = Poke.objects.all().filter(pokee=pokee)
            sum = 0
            for poke in pokes:
                sum += poke.poke_count
            return sum
        except:
            return 0


class Poke(models.Model):
    poke_count = models.IntegerField(default = 1)
    poker = models.ForeignKey(User, related_name = 'poker')
    pokee = models.ForeignKey(User, related_name = 'pokee')

    objects = PokeManager()
