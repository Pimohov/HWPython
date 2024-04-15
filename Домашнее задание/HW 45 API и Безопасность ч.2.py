# settings.py
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# import logging
# logger = logging.getLogger(__name__)
# def my_view(request):
#     logger.debug("Запрос получен")
#     # ...код вашего представления...
#     logger.info("Запрос обработан")

# views.py
# from django.shortcuts import render
# import logging.getLogger(__name__)
# def book_list(request):
#     books = Book.objects.all()
#     logger.info(f"Получено {len(books)} книг")
#     return render(request, 'books.html', {'books': books})

# MIDDLEWARE = [
# ...
# 'corsheaders.middleware.CorsMiddleWare',
# 'django.midlleware.common.CommonMiddleware',
# ...
# ]

# Custom Middleware
# class SimpleLoggingMiddleware:
#     def __int__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         print(f"Запрос{request.method} на {request.path}")
#         return response

# urls.py
# from django.urls import path, re_path
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions
#
# schema_view = get_schema_views[
#     openapi.Info(
#         title = "My Project API",
#         default_version = 'vl',
#         description = "Документации для проекта API",
#         terma_of_service = "https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@myproject.local"),
#         license=openapi.License(name="BSD License"),
#
#     ),
#     public = True
#     permissions_classes=(permissions.AllowAny,),
# )
#
# urlpatterns = [
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$',
#             schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
#     name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
#     name='schema-redoc'),
#     ...
# ]