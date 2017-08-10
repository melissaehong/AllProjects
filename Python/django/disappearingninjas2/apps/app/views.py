from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def ninjas(request):
    return render(request, 'app/ninjas.html')

def show(request, ninja_color):
    turtles = {
        'red': 'app/images/raphael.jpg',
        'orange': 'app/images/michelangelo.jpg',
        'blue': 'app/images/leonardo.jpg',
        'purple': 'app/images/donatello.jpg'
    }

    if ninja_color in turtles:
        context = {
            'image' : turtles[ninja_color]
    }
    else:
        context = {
            'image' : 'app/images/notapril.jpg'
            }

    return render(request, 'app/ninjas.html', context)

def nothing(request):
    context = {
            'image' : 'app/images/notapril.jpg'
        }
    return render(request, 'app/ninjas.html', context)
