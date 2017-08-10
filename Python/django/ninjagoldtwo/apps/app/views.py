from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'comments' not in request.session:
        request.session['comments'] = [{'style': '', 'comment': ''}]
    return render(request, 'app/index.html')

def process(request):
        if request.method == 'POST':
            goldrange = lambda x,y:random.randrange(x,y)
            data = {
            'farm':goldrange(10,20),
            'cave':goldrange(5,10),
            'house':goldrange(2,5),
            'casino':goldrange(-50,50)
            }
            try:
                request.POST['building']
                request.session['gold'] += data[request.POST['building']]
                if data[request.POST['building']] > 0:
                    style = 'Gained'
                else:
                    style = 'Lost'
                request.session['comments'].append({'style':style, 'comment':"{} {} golds from the {}!".format(style, data[request.POST['building']], request.POST['building'])})
            except:
                print 'fail'
        return redirect('/')

def reset(request):
    request.session.pop('gold')
    request.session.pop('comments')
    return redirect('/')
