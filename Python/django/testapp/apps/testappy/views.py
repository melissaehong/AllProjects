from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
    print "Index!"
    user = User.objects.login('melissahong1@gmail.com', "Melissa")

    print(type(user))
    if 'error' in user:
        pass
    if 'theuser' in user:
        pass
    return HttpResponse('Check Terminal')
