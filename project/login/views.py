from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
    context = {}
    context['title'] = 'Kirjaudu sisään'
    context['message'] = ''

    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is None:
                context['message'] = 'Väärä käyttäjätunnus tai salasana!'
            else:
                login(request, user)
                redirect('createdata:createdata', user)

    return render(request, 'login/login.html', context)