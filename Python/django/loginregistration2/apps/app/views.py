from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

# Create your views here.
def index(request):
    if 'errors' not in request.session:
        request.session['errors'] = ''
    if 'success' not in request.session:
        request.session['success'] = ''
    return render(request, 'app/index.html')

def register(request):
    if request.method == 'POST':
        User.objects.validate(request)

        result = User.objects.validateRegister(request)

        if result[0] == False:
            print request.session['errors']
            print_messages(request, result[1])
            return redirect('/')

        else:
            return log_user_in(request, result[1])

def login_user(request, user):
    user = User.objects.validateRegister(request)
    request.session['success'].append('Success! Welcome, ' + request.POST['first_name'] + '!')
    return redirect('/page')

def login(request):
    result = User.objects.validateLogin(request)

    if result[0] == False:
        print_messages (request, result[1])
        return redirect('/')
    return log_user_in(request, result[1])

def log_user_in(request, user):
    request.session['user'] = {
    'id': user.id,
    'first_name': user.first_name,
    'last_name': user.last_name,
    'email': user.email
    }
    return redirect('/page')

def page(request):
    if not 'user' in request.session:
        return redirect('/')
    if 'success' not in request.session:
        request.session['success'] = 0
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/page.html', context)

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def delete(request, id):
    deleting = User.objects.get(id = id)
    deleting.delete()
    return redirect('/page')

def logout(request):
    request.session.pop('user')
    return redirect('/')
