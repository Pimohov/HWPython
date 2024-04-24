# Задание №1
# Не смог сделать

# Задание №2
# class InventoryItem:
#     def __init__(self, name, quantity, price):
#         self.name = name
#         self.quantity = quantity
#         self.price = price
#
#     def more_product(self, amount):
#         if amount > 0:
#             self.quantity += amount
#             print(f"Количество товара {self.name} увеличено на {amount}.")
#
#     def less_product(self, amount):
#         if amount > 0 and amount <= self.quantity:
#             self.quantity -= amount
#             print(f"Количество товара {self.name} уменьшено на {amount}.")
#         else:
#             print(f"Невозможно уменьшить количество товара {self.name} на указанное количество.")
#
#     def calculate_total_value(self):
#         total_value = self.quantity * self.price
#         print(f"Общая стоимость товара {self.name}: {total_value}")
#         return total_value
#
# item1 = InventoryItem("Планшет", 10, 800)
# item2 = InventoryItem("Смартфон", 20, 400)
#
# item1.more_product(5)
# item2.more_product(10)
#
# total_value_item1 = item1.calculate_total_value()
# total_value_item2 = item2.calculate_total_value()
#
# total_inventory_value = total_value_item1 + total_value_item2
# print(f"Общая стоимость всех товаров в инвентаре: {total_inventory_value}")

# Задание №3
# class Students():
#     def __init__(self,name,grades):
#         self.name = name
#         self.grades = grades
#
#     def print_info(self):
#         print(f'Студент: {self.name}, успеваемость: {self.grades}')
#
#     def average(self):
#         aver = sum(self.grades)/len(self.grades)
#         print(f'Успеваемость: {aver}, студена: {self.name}')
#
# student1 = Students("Иван", [4,3,3,4,5,3,2,1])
# student1.print_info()
# student1.average()





