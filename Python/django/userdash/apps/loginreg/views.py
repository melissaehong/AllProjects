from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from models import User
from ..travelbuddy.models import *
import bcrypt

# Create your views here.
def index(request):
    if 'errors' not in request.session:
        request.session['errors'] = ''
    if 'success' not in request.session:
        request.session['success'] = ''
    return render(request, 'loginreg/index.html')

def register(request):
    if request.method == 'POST':
        User.objects.validate(request)

        result = User.objects.validateRegister(request)

        if result[0] == False:
            print request.session['errors']
            print_messages(request, result[1])
            return redirect('/')

        else:
            return log_user_in(request, result[1])

def signin(request):
    if request.method == 'POST':
        result = User.objects.validateLogin(request)

        if result[0] == False:
            print_messages (request, result[1])
            return redirect('/')
        return log_user_in(request, result[1])

def log_user_in(request, user):
    request.session['user_id'] = user.id
    request.session['name'] = user.name
    request.session['username'] = user.username
    return HttpResponseRedirect(reverse("travels:index"))

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
