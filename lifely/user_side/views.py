from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def dashboard(request):
    return render(request, "user_side/dashboard.html")


@login_required(login_url='login')
def events(request):
    return render(request, "user_side/events.html")


@login_required(login_url='login')
def passwords(request):
    return render(request, "user_side/password_manager.html")


# @login_required(login_url='login')
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')
