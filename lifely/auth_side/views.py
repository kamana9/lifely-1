from django.shortcuts import redirect, render
from django.views import View
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def authLogin(request):
    if request.user.is_authenticated:
        return redirect('user-dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user-dashboard')
            else:
                messages.info(request, "Username or password is incorrect.")
    context = {}
    return render(request, 'auth_side/login.html', context)


def authRegister(request):
    if request.user.is_authenticated:
        return redirect('user-dashboard')
    else:
        form = RegisterForm()

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                redirect('login')

        context = {'form': form}
        return render(request, 'auth_side/registration.html', context)
