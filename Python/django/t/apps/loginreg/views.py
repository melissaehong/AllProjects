from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from models import User
from ..travelbud.models import *
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

def login(request):
    if request.method == 'POST':
        result = User.objects.validateLogin(request)

        if result[0] == False:
            print_messages (request, result[1])
            return redirect('/')
        return log_user_in(request, result[1])

def log_user_in(request, user):
    request.session['user_id'] = user.id
    request.session['name'] = user.name
    return HttpResponseRedirect(reverse("travelbud:index"))

def success(request):
    if not 'user_id' in request.session:
        return redirect('/')
    if 'success' not in request.session:
        request.session['success'] = 0
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'loginreg/success.html', context)

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def show(request, user_id):
    user = User.objects.get(id = user_id)
    unique_ids = user.reviews_left.all().values('book').distinct()
    unique_books = []
    for book in unique_ids:
        unique_books.append(Book.objects.get(id=book['book']))
    context = {
        'user': user,
        'unique_book_reviews': unique_books
    }
    return render(request, 'loginreg/show.html', context)

def add(request):
    return render(request, 'travelbud/add.html')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def create(request):
    pass
