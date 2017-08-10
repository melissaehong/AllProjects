from django.shortcuts import render, redirect, HttpResponse
from .models import Email

# Create your views here.
def index(request):
    if not 'errors' in request.session:
        request.session['errors'] = []
    return render(request, 'emailvalid/index.html')

def process(request):
    if request.method == 'POST':
        result = Email.objects.register(request.POST['email'])
        if result[0]:
            request.session['email'] = result[1].email
            request.session.pop('errors')
            return redirect('/success')
        else:
            request.session['errors'] = result[1]
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    emails = Email.objects.all()
    return render(request, 'emailvalid/success.html', {'emails':emails, 'your_email': request.session.get('email')})

def destroy(request, id):
    result = Email.objects.destroy(id)
    if result[0]:
        return redirect('/success')
    else:
        print result[1]
