from django.contrib import admin
from testapp.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'author', 'year']
    list_filter = ['author', 'year']

admin.site.register(Book, BookAdmin)
