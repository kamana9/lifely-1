from django.urls import path
from . import views
app_name = "auth"

urlpatterns = [
    path('login', views.authLogin, name="login"),
    path('registration', views.authRegister, name="registration"),
]
