from django.contrib.auth.models import GroupManager
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import PasswordChangingForm, PasswordForm, TodosForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Passwords,Todos
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView



def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def dashboard(request):
    form = TodosForm
    if request.method == 'POST':
        form = TodosForm(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        if form.is_valid():
            form.save()
    todos = Todos.objects.filter(user=request.user).order_by('-id')
    return render(request, "user_side/dashboard.html", {
        "todos": todos,
        'form': form
    })


@login_required(login_url='login')
def events(request):
    return render(request, "user_side/events.html")


@login_required(login_url='login')
def passwords(request):
    form = PasswordForm
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        if form.is_valid():
            form.save()
    passwords = Passwords.objects.filter(user=request.user).order_by('-id')
    return render(request, "user_side/password_manager.html", {
        "passwords": passwords,
        'form': form
    })


@login_required(login_url='login')
def deleteTodo(request, pk):
    item = Todos.objects.get(id=pk)
    item.delete()
    return redirect("user-dashboard")


@login_required(login_url='login')
def deletePassword(request, pk):
    item = Passwords.objects.get(id=pk)
    item.delete()
    return redirect("user_side:user-passwords")


# @login_required(login_url='login')
class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')


class TodosList(ListView):
    model = Todos
    template_name='user_side/dashboard.html'
    context_object_name='todos'

    def post (self,request):
        title=request.POST.get('title')
        desc = request.POST.get('description')

        ins=Todos.objects.create(title=title,description=desc)
        return redirect("user_side:user-dashboard") 


        
class TodosDetail(DetailView):
    model = Todos
    template_name='user_side/todo_detail.html'
    context_object_name='todo'
class TodosUpdate(UpdateView):
    model = Todos
    fields=['title','description']
    success_url=reverse_lazy('user_side:user-dashboard')


class TodosCreate(CreateView):
    model = Todos
    fields='__all__'
    success_url=reverse_lazy('user_side:user-dashboard')
class TodosDelete(DeleteView):
    model=Todos
    fields='__all__'
    template_name='user_side/todos_delete.html'
    context_object_name='todo'
    success_url=reverse_lazy('user_side:user-todos')
    
    

class PasswordsList(ListView):
    model = Passwords
    template_name='user_side/password_manager.html'
    context_object_name='passwords' 

    def post (self,request):
        user=request.POST.get('username')
        password= request.POST.get('password')

        ins=Passwords.objects.create(username=user,password=password)
        return redirect("user_side:user-passwords") 
class PasswordsDetail(DetailView):
    model = Passwords
    template_name='user_side/password_detail.html'
    context_object_name='password'
class PasswordsUpdate(UpdateView):
    model = Passwords
    fields='__all__'
    success_url=reverse_lazy('user_side:user-passwords')

class PasswordsCreate(CreateView):
    model = Passwords
    fields='__all__'
    template_name='user_side/dashboard.html'

class PasswordsDelete(DeleteView):
    model=Passwords
    fields='__all__'
    template_name='user_side/passwords_delete.html'
    context_object_name='password'
    success_url=reverse_lazy('user_side:user-passwords')

