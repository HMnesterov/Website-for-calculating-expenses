from django.contrib import admin
from .models import Category, Item
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']

