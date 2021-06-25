from django.urls import path
from . import views
app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name='user-dashboard'),
    path('events', views.events),
    path('todo', views.todo),
    path('setting', views.setting),
    path('logout', views.logoutUser, name="logout")
]
