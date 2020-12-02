from django.contrib import admin
from .models import Category, Offers


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    prepopulated_fields = {'slug': ('category',)}


@admin.register(Offers)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'adres',
                    'image', 'bonus', 'description', 'created']
    list_filter = ['created']
    list_editable = ['bonus']
    prepopulated_fields = {'slug': ('name',)}