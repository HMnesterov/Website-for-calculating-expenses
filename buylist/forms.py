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


class ChooseDifference(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)

    start_date = forms.DateField(label='Начальная дата 1', widget=forms.TextInput(attrs={'class': 'form-input'}))
    end_date = forms.DateField(label='Конечная дата 1', widget=forms.TextInput(attrs={'class': 'form-input'}))
    start_date1 = forms.DateField(label='Начальная дата 2', widget=forms.TextInput(attrs={'class': 'form-input'}))
    end_date1 = forms.DateField(label='Конечная дата 2', widget=forms.TextInput(attrs={'class': 'form-input'}))


class DateForm(forms.Form):
    date1 = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
        , label='Please, write the first period start (Format d/m/y)'
    )

    date1_end = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
        , label='Please, write the first period end (Format d/m/y)'
    )
    date2 = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Please, write the second period start (Format d/m/y)',
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })

    )

    date2_end = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Please, write the second period end (Format d/m/y)',
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
