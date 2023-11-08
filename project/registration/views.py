from webbrowser import get
from django.shortcuts import render
from django.contrib.auth.models import User

def registration(request):
    context = {}
    context['title'] = 'Luo uusi tili'

    if request.method == 'POST':
        if 'create' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            user = User.objects.create_user(username, email, password1)

    return render (request, 'registration/registration.html', context)