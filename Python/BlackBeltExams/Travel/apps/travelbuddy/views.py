from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    print "I am index"
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'trips' : Trip.objects.filter(travelers=user),
        'other_trips': Trip.objects.all().exclude(travelers=user)
    }
    return render(request, 'travelbuddy/index.html', context)

def show(request, trip_id):
    print 'I am show'
    context = {
        'trips': Trip.objects.get(id=trip_id),
        'travelers': User.objects.filter(trip_travelers__id=trip_id)
    }
    return render(request, 'travelbuddy/show.html', context)

def add(request):
    print "I am add"
    return render(request, 'travelbuddy/add.html')

def create(request):
    errs = Trip.objects.validate_review(request.POST)
    print "I am create"
    user = User.objects.get(id=request.session['user_id'])
    if errs:
        for e in errs:
            messages.error(request, e)
        return redirect('/travels/add')
    else:
        print "I am createl"
        Trip.objects.create_trip(request.POST, user)
    return redirect('/travels')

def join(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=user_id)
    trip.travelers.add(user)
    trip.save()
    return redirect('/travels')
