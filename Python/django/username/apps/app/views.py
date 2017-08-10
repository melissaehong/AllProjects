from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
    if 'errors' not in request.session:
        request.session['errors'] = 'No errors'
    if 'success' not in request.session:
        request.session['success'] = 'None'
    return render(request, 'app/index.html')

def process(request):

    if request.method == 'POST':
        User.objects.validations(request)
        User.objects.userExists(request)

        if len(request.session['errors']) > 0:
            return redirect('/')
        else:
            User.objects.registration(request)
            request.session['success'].append('Success!  Username ' + request.POST['name'] + ' is valid!')
            return redirect('/success')

def success(request):
    if 'errors' not in request.session:
        request.session['errors'] = 'No errors'
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/success.html', context)

def delete(request, id):
    deleting = User.objects.get(id=id)
    deleting.delete()
    return redirect('/success')
