from django.shortcuts import render


def auth_login(request):
    return render(request, "auth_side/login.html")


def auth_register(request):
    return render(request, "auth_side/registration.html")
