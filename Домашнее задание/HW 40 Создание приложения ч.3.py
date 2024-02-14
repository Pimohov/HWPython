# Создание и заполнение таблиц
# from project.models import Book, Author
# author = Author.objects.get(id=1)
# book = Book(title='Название книги', author=author, published_year=2021)
# book.save()

# settings.py
# INSTALLED_APPS = [
#     'debug_toolbar',
# ]
#
# MIDDLEWARE = [
#     'debug_toolbar.middleware.DebugToolbarMiddleware'
# ]
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
# }

# BookAdmin
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_year')
#     list_filter = ('author', 'published_year')
#     search_fields = ('title', 'author__name')
# admin.site.reqister(Book, BookAdmin)

# Панель поиска
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_filter = (DecladeBornListFilter,)
#
# from django.contrib import admin
# from .models import Book
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     search_fields = ['title','author__name']

# Фильтрация
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_filter = ('published_year', 'author')

# Создание собственных фильтров
# from django.contrib import admin
# from .models import Book, Author
# from django.utils.translation import gettext_lazy as _
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_year')
#     list_filter = ('published', 'author')
#     search_fields = ['title', 'author__name']
#
# class DecadeBornListFilter(admin.SimpleListFilter):
#     title = _('decade born')
#     parameter_name = 'decade'
#
#     def lookups(self, request, model_admin):
#         return (
#             ('1950s',_(Born in the 1950s)),
#             ('1960s',_(Born in the 1960s)),
#         )
#
#     def queryset(self, request, queryset):
#         if self.value() == '1950s':
#             return queryset.filter(born__gte=1950, born__lt=1960)
#         if self.value() == '1960s':
#             return queryset.filter(born__gte=1960, born__lt=1970)