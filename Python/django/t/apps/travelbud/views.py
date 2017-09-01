from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    print "I am index"
    context = {
        'user' : Trip.objects.trip_and_trippers()[0],
        'other_users': Trip.objects.trip_and_trippers()[1]
    }
    return render(request, 'travelbud/index.html', context)

def show(request, trip_id):
    context = {
        'trip': Trip.objects.get(id=trip_id)
    }
    return render(request, 'travelbud/show.html')

def add(request):
    print "I am add"
    return render(request, 'travelbud/add1.html')

def create(request):
    errs = Trip.objects.validate_review(request.POST)
    print "I am create"
    if errs:
        for e in errs:
            messages.error(request, e)
        return redirect('/travels/add')
    else:
        print "I am createl"
        Trip.objects.create_trip(request.POST, request.session['user_id'])
    return redirect('/travels')

def join(request, user_id):
    context = {
    'tripper':Trip.objects.get(request.session['user'])
    }
    return redirect('/travels')
