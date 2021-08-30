from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LogoutView
from .views import TodosList,TodosDetail,TodosUpdate,TodosDelete,TodosCreate,PasswordsList,PasswordsUpdate,PasswordsDetail,PasswordsDelete

urlpatterns = [
    path('', TodosList.as_view(), name='user-dashboard'),
    path('todo-delete/<int:pk>/',TodosDelete.as_view(), name='user-todo-delete'),
    path('todo-create/',TodosCreate.as_view(),name="todoadd"),
    path('tododetail/<int:pk>/',TodosDetail.as_view(),name='tododetail'),     
    path('todoedit/<int:pk>/',TodosUpdate.as_view(),name="todoupdate"),

    path('events', views.events, name='user-events'),
    path('passwords', PasswordsList.as_view(), name='user-passwords'),
    path('password-delete/<int:pk>/',PasswordsDelete.as_view(), name='user-password-delete'),
    path('pdetail/<int:pk>/',PasswordsDetail.as_view(),name='password-detail'),
    path('pedit/<int:pk>/',PasswordsUpdate.as_view(),name="password-update"),
    path('logout', views.logoutUser, name='logout'),
    path('change-password/', views.PasswordChangeView.as_view(
        template_name='user_side/change_password.html'), name='password-change'),
    


]
