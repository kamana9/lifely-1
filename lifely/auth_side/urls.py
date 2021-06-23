from django.urls import path
from . import views
app_name = "auth"
urlpatterns = [
    path('login', views.auth_login, name="login"),
    path('registration', views.auth_register, name="registration")
]
