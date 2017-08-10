from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    return render(request, 'app/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['attempt'] = request.session['attempt'] + 1
        return redirect ('/result')
    return redirect ('/')

def result(request):
    return render(request,'app/results.html')
