from django.shortcuts import render, HttpResponse
import time
#CONTROLLER
# Create your views here.
def index(request):
    return render(request, 'timedisplay/index.html')

def show(request):
    return render(request, 'timedisplay/show_users.html')

def page(request):
    context = {
    'date': time.strftime("%b %d %Y"),
    'time': time.strftime("%I:%M %p")
    }
    return render(request, 'timedisplay/page.html', context)
