from django.shortcuts import render
import time

# Create your views here.
def index(request):
    context = { "currentDate":time.strftime('%b %d %Y'),
        "currentTime":time.strftime('%I:%M:%S')
        }
    return render(request, 'app/index.html', context)
