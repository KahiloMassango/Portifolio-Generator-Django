from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET


def custom_login(request):
    if request.method == "GET":
        return render(request, 'login.html')


@require_GET
def register(request):
    return render(request, 'register.html')
