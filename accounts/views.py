from django.shortcuts import render


def custom_login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
