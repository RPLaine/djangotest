from django.shortcuts import render
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

    return render (request, 'registration/registration.html', context)