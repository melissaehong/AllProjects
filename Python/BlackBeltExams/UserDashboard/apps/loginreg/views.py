from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from models import User
from ..dashboard.models import *
import bcrypt

# Create your views here.
def index(request):

    return render(request, 'loginreg/index.html')

def register(request):
    if 'errors' not in request.session:
        request.session['errors'] = ''
    return render(request, 'loginreg/register.html')

def register_user(request):
    if request.method == 'POST':
        User.objects.validate(request)

        result = User.objects.validateRegister(request)

        if result[0] == False:
            print request.session['errors']
            print_messages(request, result[1])
            return redirect('/register')

        else:
            return log_user_in(request, result[1])

def signin(request):
    if 'errors' not in request.session:
        request.session['errors'] = ''
    return render(request, 'loginreg/signin.html')

def signin_user(request):
    if request.method == 'POST':
        result = User.objects.validateLogin(request)

        if result[0] == False:
            print_messages (request, result[1])
            return redirect('/signin')
        return log_user_in(request, result[1])

def dashboard(request):
    print request.session['user_id']
    username = User.objects.get(id=request.session['user_id'])
    users = User.objects.all()
    for user in users:
        if user.user_level == 9:
            user.user_level = 'admin'
        if user.user_level == 1:
            user.user_level = 'normal'
    context = {
        'users': users,
        'user': user,
        'username': username
    }
    return render(request, 'loginreg/dashboard.html', context)

def log_user_in(request, user):
    request.session['user_id'] = user.id
    print request.session['user_id']
    return redirect('/dashboard')

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
