# Пример использования CSRF Token в шаблоне
# < form method="post">
#     {% csrf_token %}
#     <!-- Элемент -->
# </form>

# Отключение CSRF Защиты
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def home(request):
#     return HttpResponse('<hl>Главная</hl>)

# Создание простой формы
# from django import forms
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Your Name')
#     email = forms.EmailField(label='Your Email')
#     message = forms.CharField(widget=forms.Textarea, label='Your Message')

# Обработка формы в представлении
# from django.shortcuts import render
# from .froms import ContactForm
# def contact_views(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#     else:
#         form = ContactForm()
#
#     return render(request, 'contact.html', {'form': form})

# Включение формы в Шаблон
# <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Send</button>
# </form>

# Валидация данных форм
# class ContactForm(forms.Form):
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if not "example.com" in email:
#             raise forms.ValidationError("Please use your example.com email address.")
#         return email

# Итоговый файл forms.py
# from django import forms
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Your Name')
#     email = forms.EmailField(label='Your Email')
#     message = forms.CharField(widget=forms.Textarea, label='Your Message')
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if not "example.com" in email:
#             raise forms.ValidationError("Please use your example.com email address.")
#         return email

# Создание ModelForm
# from django.forms import ModelForm
# from .models import Book
# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'published_year']