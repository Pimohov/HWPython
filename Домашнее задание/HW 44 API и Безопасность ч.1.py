# Использование Фреймворков
# from rest_framework import permissions
# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user.is_admin

# Permissions
# from rest_framework import permissions
# class IsAdminOrReadyOnly(permissions.BasePermission):
#     '''
#     Разрешение, которое позволяет доступ только для чтения всем пользователям,
#     а редактирование только администраторам
#     '''
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         return request.user.is_superuser

# views.py
# from rest_framework import permissions
# from .models import Book
# from .permissions import IsAdminOrReadOnly
#
# class MyModelViewSet(Viewsets.ModelViewSet):
#     queryset = Book.object.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return DefaultSerializer
#         if self.action == 'retrieve':
#             return BookDetailSerializer
#         return DefaultSerializer

# urls.py
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter{)
# router.register{r'Book', views.MyModelViewSet)
#
# settings.py
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'project.permissions.IsAdminOrReadOnly'
#     ]
# }

# Пример кода аутентификации
# def my_login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Перенаправление на страницу успеха
#     else:
#         # Возврат ошибки аутентификации

# Пример выхода пользователя из системы
# from django.contrib.auth import logout
# def my_logout_view(request):
#     logout(request)

# settings.py
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'djoser',
#     'rest_framework_simplejwt'
#     ...
# ]
#
# REST_FRAMEWORK = {
#     ...
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#     'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#     ...
#     }
# SIMPLE_JWT = {
#     'AUTH_HEADER_TYPES': ('Bearer',),
# }

# urls.py
# from django.urls import path, include
# urlpatterns = [
# ...
# path('auth/', include('djoser.urls')),
# path('auth/', include('djoser.urls.jwt')),
# ]

# JWT Аутентификация
# from rest_framework import permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Book
#
# class BookListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request, format=None):
#         books = Book.objects.all()
#         return Response([book.title for book in books])

# settings.py
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }
# from datetime import timedelta
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': True,
# }

# Token Обработки
# from django.urls import path
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
# urlpatterns = [
#     path('api/token/', TokenObtainPairView.as_view(),
#     name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(),
#     name='token_refresh'),
# ]

# settings.py
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10
# }

# Views с Пагинацией
# from rest_framework import viewsets
# from .models import Book
# from .serializers import BookSerializer
# class BookViewsSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer