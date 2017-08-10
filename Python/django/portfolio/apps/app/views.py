from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def testimonials(request):
    return render(request, 'app/testimonials.html')

def about(request):
    return render(request, 'app/about.html')

def projects(request):
    return render(request, 'app/projects.html')
