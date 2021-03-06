from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if not 'user_id' in request.session:
        return redirect('/')

    pokes = Poke.objects.get_poked_list(request.session['user_id'])
    users = User.objects.all()
    for user in users:
        user.poke_list = Poke.objects.get_poke_list(request.session['user_id'], user.id)

    context = {
        'users': users,
        'pokes': pokes,
        'count': len(pokes)
    }
    return render(request, 'pokerapp/index.html', context)

def poke(request):
    if request.method == 'POST':
        Poke.objects.create_poke(request.POST['poker'], request.POST['pokee'])
    return redirect('pokeapp:index')
