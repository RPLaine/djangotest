from django.shortcuts import render
from django.contrib.auth.models import User

def login(request):
    context = {}
    context['title'] = 'Kirjaudu sisään'
    context['errorMessage'] = ''
    context['username'] = ''
    context['email'] = ''
    context['password'] = ''
    if (request.POST.get('username')):
        context['username'] = request.POST.get('username')
        context['email'] = request.POST.get('email')
        context['password'] = request.POST.get('password')
        print(request.POST.get('username'))

    return render(request, 'login/login.html', context)