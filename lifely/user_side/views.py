from django.shortcuts import render


def dashboard(request):
    return render(request, "user_side/dashboard.html")


def events(request):
    return render(request, "user_side/event_body.html")


def todo(request):
    return render(request, "user_side/todo_body.html")


def setting(request):
    return render(request, "user_side/setting_body.html")
