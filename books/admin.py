from django.contrib import admin
from books.models import Comment, Book

admin.site.register(Book)
admin.site.register(Comment)
