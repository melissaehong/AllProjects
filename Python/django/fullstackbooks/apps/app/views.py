from django.shortcuts import render, redirect
from models import Book

# Create your views here.
def index(request):
    books = Book.objects.all;
    context = {
        'books': books
    }
    return render(request, 'app/index.html', context)

def process(request):
    if request.method == "POST":
        Book.objects.create(title = request.POST['title'], category = request.POST['category'], author = request.POST['author'])
        return redirect('/')
