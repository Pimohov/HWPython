# Задание №1
# class ArithmeticOperations:
#     def add(self, x, y):
#         return x + y
#
#     def subtract(self, x, y):
#         return x - y
#
#     def multiply(self, x, y):
#         return x * y
#
# arithmetic_obj = ArithmeticOperations()
#
# result_plus = arithmetic_obj.add(5, 3)
# print(f"Сложение: {result_plus}")
#
# result_min = arithmetic_obj.subtract(10, 5)
# print(f"Вычитание: {result_min}")
#
# result_string = arithmetic_obj.multiply("Python ", 5)
# print(f"Умножение: {result_string}")

# Задание №2
# import math
#
# class Shape:
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
# circle = Circle(2)
# rectangle = Rectangle(2, 9)
# triangle = Triangle(3, 8)
#
# print(f"Площадь круга: {circle.area():.1f}")
# print(f"Площадь прямоугольника: {rectangle.area():.1f}")
# print(f"Площадь треугольника: {triangle.area():.1f}")

# Задание №3
# from abc import ABC, abstractmethod
#
# class Drawable(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
# class Circle(Drawable):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def draw(self):
#         print(f"Круг с радиусом {self.radius}")
#
# class Rectangle(Drawable):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def draw(self):
#         print(f"Прямоугольник шириной {self.width} и высотой {self.height}")
#
# circle = Circle(6)
# rectangle = Rectangle(4, 5)
#
# circle.draw()
# rectangle.draw()
