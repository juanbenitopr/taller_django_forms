from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, register

from books.models import Book


@register(Book)
class BookAdmin(ModelAdmin):
    pass
