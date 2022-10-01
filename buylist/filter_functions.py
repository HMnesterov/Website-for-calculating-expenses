from datetime import date, timedelta

from .models import Category


def this_day(request):
    user = request.user

    categories = user.user_category.all()
    categories_and_sum_this_day = {i: sum([f.price for f in i.category_items.all() if f.created == date.today()])
                                   for i in categories if len(i.category_items.all()) > 0}
    return categories_and_sum_this_day


def any_day_filter(request, day: int):
    user = request.user
    categories = user.user_category.all()
    categories_and_sum_14_day = {i: sum(
        [f.price for f in i.category_items.all() if date.today() - timedelta(days=day) <= f.created <= date.today()])
        for i in categories if len(i.category_items.all())}
    return categories_and_sum_14_day


def filter_categories_by_user(request):
    return Category.objects.filter(user=request.user)