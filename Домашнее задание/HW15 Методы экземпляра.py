# Задание №1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")
#
# person1 = Person("Петя", 25)
# person2 = Person("Дария", 30)
#
# person1.introduce()
# person2.introduce()

# Задание №2
# class Product:
#     def __init__(self, name, description=None, price=None):
#         self.name = name
#         self.description = description
#         self.price = price
#
#     def set_description(self, description):
#         self.description = description
#
#     def set_price(self, price):
#         if price >= 0:
#             self.price = price
#     def display_product_info(self):
#         print(f"Название: {self.name}")
#         print(f"Описание: {self.description}")
#         print(f"Цена: {self.price}")
#
# product1 = Product("Ноутбук", "Современный ноутбук", 1200)
# product2 = Product("Смартфон", "Современный смартфон с хорошей камерой", 1000)
#
# print("Информация о продукте 1:")
# product1.display_product_info()
# print("\nИнформация о продукте 2:")
# product2.display_product_info()
#
# product1.set_description("Игровой ноутбук")
# product1.set_price(2000)
#
# print("\nИнформация о продукте 1 после изменений:")
# product1.display_product_info()

# Задание №3
# class Book:
#     def __init__(self, title, author, publication_year, is_available=True):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.is_available = is_available
#
#     def checkout(self):
#         if self.is_available:
#             self.is_available = False
#             print(f"\nКнига '{self.title}' взята.")
#         else:
#             print(f"Извините, книга '{self.title}' уже недоступна.")
#
#     def checkin(self):
#         if not self.is_available:
#             self.is_available = True
#             print(f"Книга '{self.title}' возвращена в библиотеку.")
#         else:
#             print(f"Книга '{self.title}' уже доступна в библиотеке.")
#
#     def display_info(self):
#         if self.is_available:
#             status = "доступна"
#         else:
#             status = "недоступна"
#
#         print(f"\nНазвание: {self.title}\nАвтор: {self.author}\nГод выпуска: {self.publication_year}\nСтатус: {status}")
#
# book1 = Book("Белая Гвардия", "Михаил Булгаков", 1925)
# book2 = Book("1984", "Джордж Оруэлл", 1949)
#
# book1.display_info()
#
# book1.checkout()
# book1.display_info()
#
# book1.checkin()
# book1.display_info()
#
# book2.checkout()
# book2.display_info()