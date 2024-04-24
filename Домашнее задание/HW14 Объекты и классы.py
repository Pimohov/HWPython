# Задание №1
# class Car:
#     def __init__(self,brend,model,year):
#         self.brend = brend
#         self.model = model
#         self.year = year
#
#     def description(self):
#         print(f'Автомобиль марки {self.brend}, модели:{self.model}, года выпуска:{self.year}')
#
# car1 = Car('Toyota','Camry',2022)
# car2 = Car('Infiniti','FX35',2007)
#
# car1.description()
# car2.description()

# Задание №2
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Employee(Person):
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def get_info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}, Зарплата: {self.salary}")
#
# person1 = Person("Коля", 23)
# employee1 = Employee("Вася", 30, 100000)
#
# print("Информация о персоне:")
# print(f"Имя: {person1.name}, Возраст: {person1.age}")
#
# print("Информация о сотруднике:")
# employee1.get_info()

# Задание №3
# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         return "Гав!"
# class Cat(Animal):
#     def speak(self):
#         return "Мяу!"
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
# print("Dog:", dog.speak())
# print("Cat:", cat.speak())



