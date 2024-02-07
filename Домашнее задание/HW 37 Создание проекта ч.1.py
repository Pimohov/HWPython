# Функция представления
# from django.http import HttpResponse
# def index(request):
#     return  HttpResponse("Приветствую на странице")

# Параметры в функции представления
# from django.http import HttpResponse
# def green(request, name):
#     return  HttpResponse(f"Привет, {name}!")

# Передача параметров для функции
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('',views.home, name='blog-home'),
#     path('about/',views.about, name='about-club'),
#     path('time/',views.current_datetime, name='blog-home'),
#     path('greet/<str:name>/',views.greet, name='greet')
# ]

# Функция представления (views)
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('<hl>Главная</hl>')
# def about(request):
#     return HttpResponse('<hl>Вторая страница</hl>')
# def greet(request, name):
#     return HttpResponse(f'Привет, {name}!')

# Отправка маршрута
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('',views.home, name='blog-home'),
#     path('about/',views.about, name='about-club'),
#     path('greet/<str:name>/', views.greet, name='greet')
# ]

# Включение URL-представление
# from django.contrib import admin
# from django.urls import path, include
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('blog.urls')),
# ]

# Пример GET запроса
# from django.http import HttpResponse
# def get_example(request):
#     name = request.GET.get('name', 'Гость')
#     return HttpResponse(f"Привет, {name}!")

# home.html
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset='utf-8' />
#     <title>First Project</title>
# </head>
# <body>
#     <h2>Form for Users</h2>
#     <form method="post" action="postuser/">
#         {% csrf_token %}
#         <p>Name:<br> <input name="name" /></p>
#         <p>Age:<br> <input name="age" type="number" /></p>
#         <input type="submit" value="Send" />
#     </form>
# </body>
# </html>

# views.py
# def index(request):
#     return render(request, "home.html")
# def postuser(request):
#     name = request.POST.ger("name", "Undefined")
#     age = request.POST.get("age",1)
#     return HttpResponse(f"<h2>Name: {name} Age: {age}</h2>")

# urls.py
# from django.urls import path
# from . import views
#
# urlpatterns = [
# #     path('',views.home, name='blog-home'),
# #     path('about/',views.about, name='about-club'),
# #     path('time/',views.current_datetime, name='blog-home'),
# #     path('greet/<str:name>/',views.greet, name='greet')
#     path('', views.index),
#     path("postuser/", views.postuser),
# ]

# Исключение Http404
# from django.http import Http404
# def my_view(request):
#     # Код с обработкой исключений

# Обработка исключений на уровне всего приложения
# class MyExpectionMiddleware:
    # middleware код

# URLs
# from  django.conf.urls import handler404, handler500
# from myapp import views
# handler404 = views.my_custom_404_view
# handler500 = views.my_custom_error_view

# Http404
# from django.http import Http404
# from django.shortcuts import render
# def my_view(request):
#     try:
#         obj = MyModel.objects.get(pk=1)
#     except MyModel.DoesNotExist:
#         raise Http404("Объект не найден.")
#     return render(request, 'home.html', {'object': obj })

# Использование get_object_or_404
# from django.shortcuts import get_object_or_404, render
# from .models import MyModel
# def my_view(request):
#     odj = get_object_or_404(MyModel, pk=1)
#     return render(request, 'my_template.html', {'object': obj})

# Middleware для обработки исключений
# class MyExpectionMiddleware:
#     def __int__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         try:
#             response = self.get_response(request)
#         except MyCustomExpection as e:
#             return my_custom_error_handler(request, e)
#         return response