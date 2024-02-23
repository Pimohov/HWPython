# Функция authenticate
# from django.contrib.auth import authenticate
# user = authenticate(username='john', password='secret')
# if user is not None:
#     # Успешная
# else:
#     # Ошибка

# Авторизация и вход в систему
# from django.contrib.auth import login
# if user is not None:
#     login(request, user)

# Пример представления
# from django.contrib.auth import authenticate, login
# from django.shortcuts import import render, redirect
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error':'Invalid credentails'})
#
#     return render(request, 'login.html')

# Пример использования авторизации
# from django.contrib.auth.decorators import login_required, permission_required
# @login_required
# def special_view(request):
#     pass
# @permission_required('app.view_secret_data')
# def secret_data_view(request):
#     pass

# Пример URL конфигурации
# from django.contrib.auth.views import LoginView
# urlpatterns = [
#     path('login/', LoginView.as_view(), name='login'),
# ]

# LogoutView
# from django.contrib.auth.views import LogoutView
# urlpatterns = [
#     path('logout/', LogoutView.as_view(), name='logout'),
# ]

# Использование в пользовательском представлении
# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# def custom_login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'custom_login.html', {'form': form})

# Настройка формы
# <form method="post">
# #     {% csrf_token %}
# #     {{ form.as_p }}
# #     <button type="submit">Login</button>
# # </form>
# # {% if form.non_field_errors %}
# #     <div class="alert alert-danger">
# #         {{ form.non_field_errors.as_text }}
# #     </div>
# # {% endif %}

# Декоратор login_required
# from django.contrib.auth.decorators import login_required
# @login_required
# def my_view(request):
#     return render(request, 'my_template.html')

# Настройка URL для перенаправления
#
# @login_required(login_url='/custom-login/')
# def my_view(request):
#     # Код представления

# Миксин LoginRequiredMixin
# from django.contrib.auth.mixins import import LoginRequiredMixin
# from django.views.generic import TemplateView
# class MySecureView(LoginRequiredMixin, TemplateView):
#     template_name = 'my_secure_template.html'
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'

# Импорт и Создание Экзмепляра:
# from django.contrib.auth.forms import UserCreationForm
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# Шаблон для регистрации ('register.html')
# <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Register</button>
# </form>

# Настройка UserCreationForm
# from django import forms
# from django.contrib.auth.form import UserCreationForm
# from django.contrib.auth.models import User
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user

# Создание собственных разрешений
# class MyModel(models.Model):
#     # поля модели
#
#     class Meta:
#         permissions = (
#             ("can_view", "Can view MyModel"),
#             ("can_edit", "Can edit MyModel")
#         )

# Проверка разрешений в представлениях
# from django.contrib.auth.decorators import permission_required
# @permission_required('myapp.can_view', raise_exception=True)
# def my_view(request):
#     # логика представления

# Использование в Class-Based Views
# from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.views.generic import ListView
# class MyListView(PermissionRequiredMixin, ListView):
#     permission_required = 'project.can_view'

# urls.py
# urlpatterns = [
#     path('social-auth/', include('social_django.urls', namespace='social'))
#     # остальные маршруты
# ]

# Создание ссылок для входа
# <a href="{% url 'social:begin' 'google-oauth2' %}">Войти через Google</a>
# <a href="{% url 'social:begin' 'github' %}">Войти через GitHub</a>

# Настройка кэша в settings.py
# CACHES = {
#     'default':{
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient'
#         }
#     }
# }

# Интеграционный тест с Unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class MyIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.url = reverse('my_view')

    def test_view_returns_list_for_authenricated_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('object_list', response.context)
