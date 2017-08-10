from django.shortcuts import render
from random import shuffle

values = []
# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def process(request):
    if request.method == 'POST':
        values.append('Item ' + str(request.POST['number']))
        shuffle(values)
        context = {
            'number' : request.POST['number'],
            'values' : values
        }
    return render(request, 'app/results.html', context)
