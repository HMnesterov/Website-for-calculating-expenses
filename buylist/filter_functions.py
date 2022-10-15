import datetime
from datetime import date, timedelta

from .models import Category


def this_day(request):
    user = request.user

    categories = user.user_category.all()
    diction = {}
    for i in categories:
        summa = 0
        cat_itm = i.category_items.all()
        if not cat_itm:
            continue
        for j in cat_itm:
            if j.created == date.today():
                summa += j.price
        diction[i] = summa

    return diction


def any_day_filter(request, day: int):
    user = request.user

    categories = user.user_category.all()
    diction = {}
    for i in categories:
        summa = 0
        cat_itm = i.category_items.all()
        if not cat_itm:
            continue
        for j in cat_itm:
            if date.today() - timedelta(days=day) <= j.created <= date.today():
                summa += j.price
        diction[i] = summa

    return diction


def all_days(request):
    user = request.user

    categories = user.user_category.all()
    diction = {}
    for i in categories:
        summa = 0
        cat_itm = i.category_items.all()
        if not cat_itm:
            continue
        for j in cat_itm:
            summa += j.price
        diction[i] = summa
    return diction


def filter_categories_by_user(request):
    return Category.objects.filter(user=request.user)


def filter_by_two_datefields(request, obj1, obj2, obj3, obj4):
    user = request.user

    categories = user.user_category.all()
    diction = {}
    for i in categories:
        summa = 0
        cat_itm = i.category_items.all()
        if not cat_itm:
            continue
        for j in cat_itm:
            if obj1 <= j.created <= obj2:
                summa += j.price
        diction[i] = summa
    diction2 = {}
    for i in categories:
        summa = 0
        cat_itm = i.category_items.all()
        if not cat_itm:
            continue
        for j in cat_itm:
            if obj3 <= j.created <= obj4:
                summa += j.price
        diction2[i] = summa
    return (diction, diction2)



def from_str_to_datetime_obj(*args):
    return map(lambda x: datetime.date(*map(int, x.split('-'))), args)