from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


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
