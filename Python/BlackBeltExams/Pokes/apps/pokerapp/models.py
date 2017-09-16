from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

# Create your models here.
class PokeManager(models.Manager):
    def create_poke(self, poker, pokee):
        try:
            poke = Poke.objects.get(poker=poker, pokee=pokee)
            poke.poke_count += 1
            poke.save()
        except:
            poker_user = User.objects.get(id=poker)
            pokee_user = User.objects.get(id=pokee)
            poke = Poke.objects.create(poker=poker_user, pokee=pokee_user)
        return poke

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
