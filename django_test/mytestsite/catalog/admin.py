from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Languages

# Register your models here.

# admin.site.register(Book)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0
    # list_display = ('title', 'display_genre')
    fields = ('title', "summary")
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    ordering = ['book__title', 'status']
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
admin.site.register(Languages)