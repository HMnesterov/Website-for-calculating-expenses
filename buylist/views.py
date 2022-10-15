import datetime

from .filter_functions import any_day_filter, this_day, filter_categories_by_user, all_days, filter_by_two_datefields, \
    from_str_to_datetime_obj
from django.contrib.auth import login, logout

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.contrib import messages

from .forms import ItemForm, CategoryForm, RegisterForm, LoginForm, ChooseDifference, DateForm


def start(request):
    if request.user.is_authenticated:
        queryset = this_day(request)
        return render(request, 'shablons/start_page.html',
                      {'values': queryset})
    return render(request, 'shablons/start_page.html')

@login_required(login_url=reverse_lazy('login'))
def filter_by_days(request, days):
    if request.user.is_authenticated:
        queryset = any_day_filter(request, days)

        return render(request, 'shablons/start_page.html',
                      {'values': queryset, 'type': 'категориям'})

    return redirect('start')


@login_required(login_url=reverse_lazy('login'))
def add_item(request):
    form = ItemForm()

    form.fields['category'].queryset = filter_categories_by_user(request)

    if request.method == 'POST':
        try:

            form = ItemForm(request.POST)

            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request=request, message='Item was added!')
                return redirect('start')

        except:
            return HttpResponse('Ой, что-то пошло не так!')

    return render(request, 'shablons/add_item.html', {'form': form, 'add': 'Item'})


@login_required(login_url=reverse_lazy('login'))
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':

        try:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, ' Category was added!')
                return redirect('start')

        except:
            return HttpResponse('Something goes wrong')

    return render(request, 'shablons/add_item.html', {'form': form, 'add': 'Category'})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':

        try:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request=request, user=user)
                return redirect('start')

        except:
            return HttpResponse('Ой, что-то пошло не так!')
    return render(request, 'shablons/register.html', {'form': form})


def authorization(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)
            messages.success(request, 'Sign completed successfully')
            return redirect('start')

    return render(request, 'shablons/register.html', {'form': form})

@login_required(login_url=reverse_lazy('login'))
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url=reverse_lazy('login'))
def see_difference_between_values(request, queryset1, queryset2, queryset3, queryset4):
    queryset1, queryset2, queryset3, queryset4 = from_str_to_datetime_obj(queryset1, queryset2, queryset3, queryset4)
    stats1, stats2 = filter_by_two_datefields(request, queryset1, queryset2, queryset3, queryset4)


    return render(request, 'shablons/difference.html', {'stats1': stats1, 'stats2': stats2})

@login_required(login_url=reverse_lazy('login'))
def SeeDifference(request):
    form = DateForm()
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            return redirect('difference', queryset1=form.cleaned_data['date1'],
                            queryset2=form.cleaned_data['date1_end'], queryset3=form.cleaned_data['date2']
                            , queryset4=form.cleaned_data['date2_end'])

    return render(request, 'shablons/test.html', {'form': form})
