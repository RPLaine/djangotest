from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import LoginForm

def login(request):
    form = LoginForm()

    context = {}
    context['title'] = 'Login'

    return render(request, 'login/login.html', context)