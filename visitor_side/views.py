from django.shortcuts import render
from .forms import FeedbackForm, NewsLetterForm


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        form = FeedbackForm
        newsletter_form = NewsLetterForm
    return render(request, "visitor_side/index.html", {
        'form': form,
        'newsletter_form': newsletter_form
    })


def about_us(request):
    return render(request, "visitor_side/about_us.html")


def blog(request):
    return render(request, "visitor_side/blog.html")

