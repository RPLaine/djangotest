from django.shortcuts import render

def registration(request):
    context = {}
    context['title'] = 'Luo uusi tili'

    return render (request, 'registration/registration.html', context)