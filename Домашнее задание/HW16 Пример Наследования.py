# Задание №1
# class Vehicle:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
# class Car(Vehicle):
#     def __init__(self, model, year, fuel_type):
#         super().__init__(model, year)
#         self.fuel_type = fuel_type
#
# vehicle1 = Vehicle("Generic Model", 2022)
# car1 = Car("Toyota Camry", 2023, "Gasoline")

# Задание №2
# from abc import ABC, abstractmethod
#
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
# class Flyable(ABC):
#     @abstractmethod
#     def fly(self):
#         pass
#
# class Bird(Animal, Flyable):
#     def __init__(self, species, name):
#         super().__init__(species)
#         self.name = name
#
#     def fly(self):
#         print(f"{self.species} по имени {self.name} летит.")
#
# bird1 = Bird("Птица", "Скворец")
# bird1.fly()

