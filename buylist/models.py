from django.contrib.auth.models import User
from django.db import models

from django.core.validators import MinValueValidator



class Category(models.Model):
    category_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')

    def __str__(self):
        return self.category_name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_items')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_items')
    name = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(validators=[MinValueValidator(0.00000001)])
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.price})"





