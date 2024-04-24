# Задание №1
# students = {
#     'Olga':'Троечница',
#     'Vasya':'Отличник',
#     'Pasha':'Троечник',
#     'Valera':'Ударник',
# }
# for key,value in students.items():
#     print(key,'-',value)

# Задание №2
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# union = set1 | set2
# intersection = set1 & set2
# print("Пересечение множеств:", intersection)
# print("Объединение множеств:", union)

# Задание №3
# countries_cities = {'Russia':input('Город России - '), 'Germany':input('Город Германии - '), 'Poland':input('Город Польши - ')}
# for key, value in countries_cities.items():
#     print(f'Страна:{key},город:{value}')

# Задание №4
# inventory = {2019090100:'Школьный рюкзак. Кол-во: 1шт. Цена: 10000тг',
#              2023021001:'Букет Роз, Средний. Кол-во: 1. Цена: 14000тг',
#              2020123120:'Набор новогодних игрушек. Кол-во: 2шт. Цена: 3000тг'
# }
# for key, value in inventory.items():
#     print(key,'------->',value)

# Задание №5
# def find_inventory():
#     name = int(input('Введите ключ:'))
#     inventory = {2019090100: 'Школьный рюкзак. Кол-во: 1шт. Цена: 10000тг',
#              2023021001: 'Букет Роз, Средний. Кол-во: 1. Цена: 14000тг',
#              2020123120: 'Набор новогодних игрушек. Кол-во: 2шт. Цена: 3000тг'
#     }
#     if name in inventory:
#         print(inventory[name])
# find_inventory()

# Задание №6
# inventory = {'Цена 1 товара':10000,
#              'Цена 2 товара':14000,
#              'Цена 3 товара':3000
# }
# def sum_inventory():
#     summa = 0
#     for i in inventory.values():
#         summa += i
#     print(summa)
# sum_inventory()

# Задание №7
# set1 = {1,23,4,5,6,78,8}
# set2 = {34,45,65,2,21,4,5}
# print('Разность',set1.difference(set2))
# print('Общие',set1.union(set2))

# Задание №8
# def find_per(set1, set2):
#     print('Пересечение', set1 & set2)
# find_per({9,47,11,15,7,6,9},{47,12,82,6,9,0,11})

# Задание №9
# def find_ob(set1, set2):
#     union = set1 | set2
#     print('Объединение', union)
# find_ob({1,2,3,4,5,6,7,8},{6,7,8,9,10,11,12})