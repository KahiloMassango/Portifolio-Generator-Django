from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
# from django.views.decorators.http import require_POST
from django.http import Http404


def custom_login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def register_create(request):
    if request.method != 'POST':
        return Http404
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return redirect('accounts:login')
    else:
        return redirect('accounts:register')
