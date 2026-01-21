from django.contrib import admin
from book.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_date', 'isbn_number')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre', 'published_date')