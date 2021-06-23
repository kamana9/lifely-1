from django.shortcuts import render
# from django.http import HttpResponse
# from django .views .generic .list import ListView
# from .models import Aboutus


def index(request):
    return render(request, "visitor_side/index.html")


def about_us(request):
    return render(request, "visitor_side/about_us.html")


def blog(request):
    return render(request, "visitor_side/blog.html")
