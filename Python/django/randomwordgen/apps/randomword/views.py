from django.shortcuts import render, redirect

import random
import string

def random_string(length):
    pool = string.letters + string.digits
    return ''.join(random.choice(pool) for i in xrange(length))
# Create your views here.
def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    return render(request, 'randomword/index.html')

def create(request):
    print(request.method)
    if request.method == 'POST':
        print('*'*50)
        print (request.POST)
        print('*'*50)
        request.session['number'] = random_string(13)
        request.session['attempt'] += 1
        return redirect('/')
    else:
        return redirect('/')
