from django.shortcuts import render, redirect
from models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'app/index.html', context)

def process(request):
    if request.method == 'POST':
        Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect ('/')

def delete(request, id):
    course_to_delete = Course.objects.get(id=id)
    context = {
        'course': course_to_delete
    }
    if request.method == 'GET':
        return render(request, 'app/delete.html', context)

    course_to_delete.delete()
    return redirect('/')
