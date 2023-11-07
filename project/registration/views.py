from django.shortcuts import render

def registration(request):
    context = {}

    return render (request, 'registration/registration.html', context)