from django import forms
from django.contrib.auth.models import User

from .models import Category, Item
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(label='Category')

    class Meta:
        model = Category
        fields = ['category_name']


class ItemForm(forms.ModelForm):
    name = forms.CharField(label='Name (not necessarily)')

    class Meta:
        model = Item
        fields = ['category', 'name', 'price']


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password']
