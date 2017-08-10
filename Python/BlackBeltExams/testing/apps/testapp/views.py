from django.shortcuts import render
from .models import User, Post

# Create your views here.
def index(request):
    return render(request, 'testapp/index.html')
