from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
    try:
        request.session['comments']
    except:
        request.session['comments'] = [{'style': 'white', 'comment': 'Activities:'}]
    return render(request, 'ninjago/index.html')

def money(request):
    if request.method == 'POST':
        mymap = lambda x,y:random.randrange(x,y)
        data = {
        'farm':mymap(10,20),
        'cave':mymap(5,10),
        'house':mymap(2,5),
        'casino':mymap(-50,50)
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
