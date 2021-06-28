from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='user-dashboard'),
    path('events', views.events),
    path('todo', views.todo),
    path('setting', views.setting),
    path('logout', views.logoutUser, name="logout"),
    path('change-password/', views.PasswordChangeView.as_view(
        template_name='user_side/change_password.html'), name='password-change')
]
