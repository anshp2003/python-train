from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, genres, Book, BorrowedRecord

admin.site.register(Author)
admin.site.register(genres)
admin.site.register(Book)
admin.site.register(BorrowedRecord)
