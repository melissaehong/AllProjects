from django.shortcuts import render, redirect

def index(request):
    return render(request, 'surveyformapp/index.html')

def process(request):
    print(request.method)
    if request.method == 'POST':
        print ('*'*50)
        print (request.POST)
        print ('*'*50)
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['optional'] = request.POST['optional']
        request.session['attempt'] += 1
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'surveyformapp/result.html')

# Create your views here.
