from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['user_id'])
    users = User.objects.all()
    context = {
        'user': user,
        'users': users,
    }
    return render(request, 'pokeapp/index.html', context)

def poke(request, owner_id):
    if request.method == 'POST':
        pokee = User.objects.get(id=owner_id)
        poker = User.objects.get(id = request.session['user_id'])
        request.POST = request.POST.copy()
        Poke.objects.create(poker = poker, pokee = pokee)
    return redirect('pokeapp:show', id=owner_id)

def show(request, id):
    context = {
    }
    return redirect(reverse('pokeapp:index'), context)
