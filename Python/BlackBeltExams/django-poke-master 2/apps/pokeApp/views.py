from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User, Poke

def main(request):
    return render(request, 'pokeApp/main.html')

def register(request):
    data = User.objects.isValidRegistration(request)
    if data[0] == False:
        print_messages(request, data[1])
        return redirect(reverse('main'))
    return log_user_in(request, data[1])

def login(request):
    data = User.objects.isValidLogin(request)
    if data[0] == False:
        print_messages(request, data[1])
        return redirect(reverse('main'))
    return log_user_in(request, data[1])

def log_user_in(request, user):
    request.session['user'] = {
        'id' : user.id,
        'name' : user.name,
        'alias' : user.alias,
        'email' : user.email,
    }
    return redirect(reverse('pokes'))

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.ERROR, message)

def logout(request):
    request.session.pop('user')
    return redirect(reverse('main'))



def pokes(request):
    if not 'user' in request.session:
        return redirect(reverse('main'))
    pokes = Poke.objects.get_poked_history(request.session['user']['id'])

    users = User.objects.all()
    for user in users:
        user.poke_history = Poke.objects.get_poke_history(request.session['user']['id'], user.id)
    context = {
        "users" : users,
        "pokes" : pokes,
        "count" : len(pokes)
    }
    return render(request, 'pokeApp/pokes.html', context)


def action(request):
    Poke.objects.poking(request.POST['from_user'], request.POST['to_user'])
    return redirect(reverse('pokes'))
