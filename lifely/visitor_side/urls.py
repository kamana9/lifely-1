from django.urls import path
from .views import index, about_us, blog
app_name = "index"

urlpatterns = [
    path('', index, name="index1"),
    path('about', about_us, name="about"),
    path('blog', blog, name="blog")
]
