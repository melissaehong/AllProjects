from django.shortcuts import render
import random
image = ''

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def landscapes(request, number):
    global image
    number = int(number)
    if number < 1 or number > 50:
        imagee = ''
    if number < 11:
        imagee = 'app/images/snow1.jpeg'
    elif number < 21:
        imagee = 'app/images/desert.jpeg'
    elif number < 31:
        imagee = 'app/images/forest.jpeg'
    elif number < 41:
        imagee = 'app/images/vineyard.jpeg'
    elif number < 51:
        imagee = 'app/images/tropical.jpeg'
    context = {
        'imagee': imagee
    }
    return render(request, 'app/landscapes.html', context)
