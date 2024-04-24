# Задание №1
# import math
# R = int(input('Введите радиус: '))
# res = math.pi * math.pow(R,2)
# print(f'Площадь = {res:.2f}')

# Задание №2
# import math
# def average(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             return False
#     return True
# num = int(input("Введите число: "))
# if average(num):
#     print(f"{num} - простое число")
# else:
#     print(f"{num} - не простое число")

# Задание №3
# def S(base, height):
#     area = 0.5 * base * height
#     return area
#
# base = float(input("Введите длину основания треугольника: "))
# height = float(input("Введите высоту треугольника: "))
# result = S(base, height)
# print(f"Площадь треугольника: {result}")

# Задание №4
# import datetime
# now = datetime.date.today()
# new_date = now + datetime.timedelta(days=7)
# print("Дата через 7 дней:", new_date)

# Задание №5
# import datetime
# def days_between_dates(date1, date2):
#     delta = date2 - date1
#     return delta.days
#
# date_str1 = input('Введите первую дату: ')
# date_str2 = input('Введите вторую дату: ')
# date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
# date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
# days_difference = days_between_dates(date1, date2)
# print(f'Количество дней между датами: {days_difference} дней')

# Задание №6
# import datetime
# date_str = input("Введите дату: ")
# date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
# day_of_week = date.strftime("%A")
# print(day_of_week)

# Задание №7
# import random
# random_number = random.randint(1, 6)
# guess = int(input("Загадайте число от 1 до 6: "))
# if guess == random_number:
#     print(f"Поздравляем! Вы угадали число: {random_number}")
# else:
#     print(f"Выпало число: {random_number}, попробуйте еще раз!")
# Задание №9
# import random
# people = ["Петя", "Коля", "Вася", "Оля", "Маша"]
# winner_index = random.randint(0, len(people) - 1)
# winner = people[winner_index]
# print(winner)

# Задание №10
# import time
# min = 60
# start_time = time.time()
# while time.time() - start_time < min:
#     current_time = time.strftime("%H:%M:%S")
#     print(current_time)
#     time.sleep(1)