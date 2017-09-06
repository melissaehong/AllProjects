from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from ..loginreg.models import *
from ..loginreg.views import *

# Create your views here.
def add(request, id):
    user = User.objects.get(id=id)
    print user.user_level
    if user.user_level == 9:
        return render(request, 'dashboard/add.html')
    return redirect('/dashboard')

def create(request):
    if request.method == 'POST':
        User.objects.validate(request)

        result = User.objects.validateRegister_User(request)

        if result[0] == False:
            print request.session['errors']
            print_messages(request, result[1])
            return redirect('/register')

    return redirect('/dashboard')

def profile(request, id):
    user = User.objects.get(id=id)
    context = {
        'user':user
    }
    return render(request, 'dashboard/profile.html', context)

def show(request, id):
    user = User.objects.get(id=id)
    users = User.objects.all()
    messages = Message.objects.all()
        
    context = {
        'user':user,
        'users': users,
        'messages': messages
    }
    return render(request, 'dashboard/show.html', context)

def message(request, id):
    user = User.objects.get(id=id)
    Message.objects.create(message = request.POST['message'], user = user)
    return redirect('/dashboard')

def comment(request, id):
    pass

def edit(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'dashboard/editprofile.html', context)

def edit_user(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'dashboard/edituser.html', context)

def update(request, id):
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(5))
    user_to_update = User.objects.get(id=id)
    print user_to_update.id
    user_to_update.first_name = request.POST['first_name']
    user_to_update.last_name = request.POST['last_name']
    user_to_update.email = request.POST['email']
    user_to_update.password = pw_hash
    user_to_update.save()
    return redirect('/dashboard')

def delete(request, id):
    user_to_delete = User.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'dashboard/remove.html', {'user': user_to_delete})
    user_to_delete.delete()
    return redirect('/dashboard')
