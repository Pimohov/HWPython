# Рендеринг шаблонов
# from django.shortcuts import render
# def my_view(request):
#     context = {'user':request.user}
#     return render(request, 'my_template.html', context)

# Добавление рендеринга
# def home_view(request):
#     context = {
#         'title': 'Главная страница',
#         'description': 'Это описание главной страницы.'
#     }
#     return render(request, 'home.html', context)

# Заполнение home.html
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="utf-8" />
#     <title>{{ title }}</title> #
# </head>
# <body>
#     <hl>{{ title }}</hl> #
#     <p>{{ description }}</p> #
#     <form method="post" action="postuser/">
#         {% csrf_token %}
#         <p>Name:<br> <input name="name" /></p>
#         <p>Age:<br> <input name="age" type="number" /></p>
#         <input type="submit" value="Send" />
#     </form>
# </body>
# </html>

# Использование циклов и условий
# def products_view(request):
#     products = [
#         {'name': 'Продукт 1', 'price': 150},
#         {'name': 'Продукт 2', 'price': 300},
#         {'name': 'Продукт 3', 'price': 450}
#     ]
# return render(request, 'products.html', {'products': products})

# Описание products.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Продукты</title>
# </head>
# <body>
#     <hl>Список продуктов</hl>
#     {% if products %}
#         <ul>
#             {% for product in products %}
#                  <li>{{ product.name }} - {{ product.price }} kzt.</li>
#             {% endifor %}
#         </ul>
#     {% else %}
#           <p>Продукты отсутствуют.</p>
#     {% endif %}
# </body>
# </html>

# Пример кода base.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>{% block title %}Мой сайт{% endblock %}</title>
# </head>
# <body>
#     <header>
#         <hl>Добро пожаловать на мой сайт</hl>
#     </header>
#
#     <main>
#         {% block content %}
#         {% endblock %}
#     </main>
#
#     <footer>
#         <p>2024 Мой сайт</p>
#     </footer>
# </body>
# </html>

# Дочерний шаблон about.html
# {% extends 'base.html' %}
# {% block title %}О сайте{% endblock %}
# {% block content %}
#     <h2>О сайте</h2>
#     <p>Это страница о нашем великолепном сайте.</p>
# {% endblock %}

# Создание собственного фильтра
# from django import template
#
# register = template.Library()
# @register.filter(name='capitalize')
# def capitalize(value):
#     return value.title()

# Использование фильтра в шаблоне text.html
# def Text(request):
#     context = {
#         'my_text': 'The kindness is brilliant of heart, Its highter than mountains around.'
#     }
#     return render(request, 'text.html', context)

# Пример тэга
# from  django import template
# register = template.Library()
# @register.simple_tag
# def my_simple_tag(a,b):
#     return a + b

# Пример Inclusion Tag
# from django import template
# register = template.Library()
# @register.inclusion_tag('my_template.html')
# def my_inclusion_tag(some_list):
#     return  {'some_list':some_list}

