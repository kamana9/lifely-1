from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import PasswordResetEmail
from . import views

urlpatterns = [
    path('login', views.authLogin, name="login"),
    path('registration', views.authRegister, name="registration"),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="auth_side/password_reset.html",
        form_class=PasswordResetEmail
    ),
        name="reset_password"),

    path('reset_password_sent/',  auth_views.PasswordResetDoneView.as_view(
        template_name="auth_side/password_reset_sent.html"
    ),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="auth_side/password_reset_form.html",
    ),
        name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="auth_side/password_reset_done.html",
    ),
        name="password_reset_complete"),
]
