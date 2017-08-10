from django.shortcuts import render, redirect
from models import Product

# Create your views here.
def users(request):
    if request.method == "POST":
        return create(request)
    return index(request)

def users_w_id(request, id):
    if request.method == "POST":
        return update(request, id)
    return show(request, id)

def index(request):
    products = Product.objects.all()
    return render(request, 'products_app/index.html', {'products': products})

def create(request):
    Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    return redirect('/products')

def new(request):
    return render(request, 'products_app/new.html')

def show(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products_app/show.html', { 'product' : product })

def update(request, id):
    Product.objects.update(id, request.POST)
    return redirect('/products')

def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products_app/edit.html', { 'product' : product})

def destroy(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/products')
