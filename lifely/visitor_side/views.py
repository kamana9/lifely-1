from django.shortcuts import render
from .forms import FeedbackForm
# from django.http import HttpResponse
# from django .views .generic .list import ListView
# from .models import Aboutus


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm
    return render(request, "visitor_side/index.html", {
        'form': form
    })


def about_us(request):
    return render(request, "visitor_side/about_us.html")


def blog(request):
    return render(request, "visitor_side/blog.html")
