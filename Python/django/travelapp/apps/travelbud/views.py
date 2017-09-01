from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    print "I am index"
    context = {
        'users' : Trip_Review.objects.trip_and_trippers()[0],
        'other_users': Trip_Review.objects.trip_and_trippers()[1]
    }
    return render(request, 'travelbuddy/index.html', context)

def show(request, trip_id):
    print 'I am show'
    context = {
        'trips': Trip_Review.objects.get(id=trip_id)
    }
    return render(request, 'travelbud/show.html', context)

def add(request):
    print "I am add"
    return render(request, 'travelbud/add.html')

def create(request):
    errs = Trip_Review.objects.validate_review(request.POST)
    print "I am create"
    if errs:
        for e in errs:
            messages.error(request, e)
        return redirect('/travels/add')
    else:
        print "I am createl"
        Trip_Review.objects.create_trip(request.POST, request.session['name'])
    return redirect('/travels')

def join(request, user_id):
    context = {
    'tripper':Trip_Review.objects.get(request.session['user'])
    }
    return redirect('/travels')
