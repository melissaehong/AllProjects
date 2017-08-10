from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    return render(request, 'app/index.html')

def create(request):
    if request.method == 'POST':
        request.session['randomWord'] = randomString(14)
        request.session['attempt'] = request.session['attempt'] + 1
        return redirect('/')
    else:
        return redirect('/')

def randomString(length):
    letternumber = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(letternumber) for i in xrange(length))
