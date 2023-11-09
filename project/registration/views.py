from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def registration(request):
    context = {}
    context['title'] = 'Luo uusi tili'
    context['errorMessage'] = ''

    if request.method == 'POST':
        if 'create' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if (User.objects.filter(username=username).exists() or User.objects.filter(email=email)):
                context['errorMessage'] = 'Käyttäjätunnus tai sähköpostiosoite on jo olemassa!'
            else:
                if (password1 != password2):
                    context['errorMessage'] = 'Salasanat eivät täsmää!'
                else:
                    User.objects.create_user(username, email, password1)
                    redirect('login:login', username=username, email=email, password=password1)

    return render (request, 'registration/registration.html', context)