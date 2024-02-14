# Пример дефолтной модели
# from django.db import models
# class MyModel(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.title

# Пример определения класса Meta
# from django.db import models
# class MyModel(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "My Model"
#         verbose_name_plural = "My Models"
#         ordering = ['-created_at']

# models.py
# from django.db import models
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     published_year = models.IntegerField()
#     def __str__(self):
#         return self.title

# models.py
# from django.db import models
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     published_year = models.IntegerField()
#     class Meta:
#         db_table = 'book'

# views.py
# from .models import Book
# def show_books(request):
#     books = Book.objects.all()
#     return render(request, 'project/books_list.html', {'books': books})

# books_list.html
# <!-- books_list.html -->
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meat charset="UTF-8">
#     <title>Books List</title>
# </head>
# <body>
#     <hl>Books List</hl>
#     {% if books %}
#         <ul>
#             {% for book in books %}
#             <p>{{ book.title }} - {{ book.author }}</p>
#         {% endfor %}
#         </ul>
#     {% else %}
#         <p>No books available.</p>
#     {% endif %}
# </body>
# </html>

# Slug Field
# class Book(models.Model):
#     title = models.CharField(max_lenght=100)
#     author = models.CharField(max_lenght=100)
#     published_year = models.IntegerField()
#     def get_absolute_url(self):
#         return reverse('book-detail', kwargs={'slug': self.slug})

# ForeignKey
# class Author(models.Model):
#     name = models.CharField(max_length=100)
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)

# ManyToManyField
# class Genre(models.Model):
#     name = models.CharField(max_length=100)
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     genres = models.ManyToManyField(Genre)

# OneToOneField
# class BookDetail(models.Model):
#     book = models.OneToOneField(Book, on_delete=models.CASCADE)
#     summary = models.TextField()
#     cover = models.ImageField(upload_to='covers/')

# Класс Q для сложных запросов
# from django.db.models import Q
# books = Book.objects.filter(Q(author='Author 1') | Q(author='Author 2'))
# books = Book.objects.filter(Q(published_year__lt=2000) & ~Q(author='Author 1'))

# Класс F для сравнения полей модели
# from django.db.models import F
# Book.objects.update(published_year=F('published_year') + 1)
# books = Book.objects.filter(published_year__gt=F('another_year_field'))

# Метод annotate для агрегации данных
# from django.db.models import Count,Avg
# authors = Author.objects.annotate(num_books=Count('book'))
# authors = Author.objects.annotate(average_year=Avg('book__published_year'))

# Использование функции агрегации в запросах
# from django.db.models import Count
# authors_with_book_count = Author.objects.annotate(num_books=Count('book'))
# for author in authors_with_book_count:
#     print(f"{author.name} has written {author.num_books} books")

