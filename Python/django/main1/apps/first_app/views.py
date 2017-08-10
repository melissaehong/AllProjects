from django.shortcuts import render, HttpResponse

# controller

def index(request):
    print "*"*50
    return render(request, 'first_app/index.html')

# Create your views here.
