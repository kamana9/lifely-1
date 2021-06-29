from django import forms
from .models import FeedBacks, NewsLetter


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBacks
        fields = '__all__'
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Full Name', 'class': 'w-full bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', }))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Your Email', 'class': 'w-full bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Your Message', 'class': 'w-full bg-white rounded border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out', }))


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Your Email', 'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:bg-transparent focus:ring-2 focus:ring-blue-200 focus:border-blue-500 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', }))
