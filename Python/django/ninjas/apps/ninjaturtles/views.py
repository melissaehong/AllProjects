from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjaturtles/index.html')

def show(request, ninja_color):
    turtle_options = {
        'red' : 'ninjaturtles/raphael.jpg',
        'blue' : 'ninjaturtles/leonardo.jpg',
        'orange' : 'ninjaturtles/michelangelo.jpg',
        'purple' : 'ninjaturtles/donatello.jpg'
    }

    if ninja_color in turtle_options:
        context = {
        'image': turtle_options[ninja_color]
        }
    else:
        context = {
            'image':'ninjaturtles/notapril.jpg'
        }
    return render(request, 'ninjaturtles/index.html', context)
