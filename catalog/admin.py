from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')  # дополнительная информация
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]  # изменение расположения


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')  # дополнительная информация
    list_filter = ('genre', 'author')  # фильтрация в панели администратора
    inlines = [BookInstanceInline]


@admin.register(BookInstance)  # заменяет admin.site.register
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')  # фильтрация в панели администратора
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back')
        })
    )


# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
# admin.site.register(BookInstance)
# admin.site.register(BookInstance, BookInstanceAdmin)

# Register your models here.
