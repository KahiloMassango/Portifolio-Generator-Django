from django.shortcuts import render
from .forms import LoginForm


def custom_login(request):
    form = LoginForm

    return render(request, 'login.html', {'form': form})


def register(request):
    return render(request, 'register.html')
