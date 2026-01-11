from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'is_available', 'published_date']
    list_filter = ['genre', 'is_available', 'published_date']
    search_fields = ['title', 'author']
    list_per_page = 20
