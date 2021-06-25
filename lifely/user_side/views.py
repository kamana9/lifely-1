from django.shortcuts import redirect, render
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


def logoutUser(request):
    logout(request)
    return redirect("auth:login")


@login_required(login_url='auth:login')
def dashboard(request):
    return render(request, "user_side/dashboard.html")


@login_required(login_url='auth:login')
def events(request):
    return render(request, "user_side/event_body.html")


@login_required(login_url='auth:login')
def todo(request):
    return render(request, "user_side/todo_body.html")


@login_required(login_url='auth:login')
def setting(request):
    return render(request, "user_side/setting_body.html")
