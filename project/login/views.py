from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    context = {}
    context['title'] = 'Kirjaudu sisään'
    context['message'] = ''
    context['username'] = ''
    context['password'] = ''
    if (request.POST.get('username')):
        context['username'] = request.POST.get('username')
        context['password'] = request.POST.get('password')
        print(request.POST.get('username'))

    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if (User.objects.filter(username=username).exists()):
                user = User.objects.get(username=username)
                if (user.check_password(password)):
                    redirect('createdata:createdata', user)
                else:
                    context['message'] = 'Väärä käyttäjätunnus tai salasana!'
            else:
                context['message'] = 'Väärä käyttäjätunnus tai salasana!'

    return render(request, 'login/login.html', context)