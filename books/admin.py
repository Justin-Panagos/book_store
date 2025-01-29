from django.contrib import admin

from books.models import Book



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "subtitle" ,
        "author" ,
        "isbn" ,
    ]
