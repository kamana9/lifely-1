from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Passwords, Todos
from django.views.generic.edit import FormView


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Old Password', 'class': 'w-full mx-auto bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'New Password', 'class': 'w-full mx-auto bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'w-full mx-auto bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ['username', 'password']
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'class': 'w-full bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', }))
    password = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Password', 'class': 'w-full bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', }))


class TodosForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['title', 'description']
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Title', 'class': 'w-full bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Description', 'class': 'w-full bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', }))
