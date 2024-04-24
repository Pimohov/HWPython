# x = int(input("Введите число: "))
# if x > 0:
#     print("Положительное число")
# if x < 0:
#     print("Отрицательное число")
# if x == 0:
#     print("Ноль")

# Программа с двумя числами:
# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print("Число a больше чем b")
# elif a < b:
#     print("Число b больше чем a")
# elif a == b:
#     print("Число a равно b")

# Проверка диапазона:
# a = int(input("Введите число: "))
# if a >= 10 and a <= 20:
#     print("Число лежит в диапазоне от 10 до 20")
# else:
#     print("Число не лежит в диапазоне от 10 до 20")

# Программа с вождением автомобиля:
# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Вы можете водить автомобиль")
# else:
#     print("Вы не можете водить автомобиль")

# Программа с оценкой:
# grade = int(input("Введите оценку: "))
# if grade == 5:
#     print("Отлично")
# elif grade == 4:
#     print("Хорошо")
# elif grade == 3:
#     print("Удовлетворительно")
# elif grade == 1 or grade == 2:
#     print("Неудовлетворительно")
# else:
#     print("Недопустимое значение оценки")

# Программа с возрастом:
# age = int(input("Введите свой возраст: "))
# if age < 2 and age >= 0:
#     print("Младенец")
# if age >= 2 and age < 12:
#     print("Ребёнок")
# if age >= 12 and age < 18:
#     print("Подросток")
# if age >= 18 and age < 35:
#     print("Молодёжь")
# if age >= 35 and age < 60:
#     print("Взрослый")
# if age >= 60:
#     print("Пожилой")

# Четверти:
# number = int(input("Введите число: "))
# if number > 0 and number <= 25:
#         print("Число находится в первой четверти.")
# elif number > 25 and number <= 50:
#         print("Число находится во второй четверти.")
# elif number > 50 and number <= 75:
#         print("Число находится в третьей четверти.")
# elif number > 75 and number <= 100:
#         print("Число находится в четвертой четверти.")
# else:
#     print("Число находится вне четвертей.")

# Четное или нечетное:
# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print("Число четное!")
#     if number % 4 == 0:
#         print("Число делится на 4")
#     else:
#         print("Число не делится на 4")
# else:
#     print("Число нечетное")

# Оценка с проверкой на доп.задание:
# grade = int(input("Введите оценку: "))
# if grade > 0 and grade <= 4:
#     print('''Совсем неудовлетворительно
# Имеется ли у ученика дополнительная работа?''')
# elif grade > 4 and grade <= 6:
#     print("Неудовлетворительно")
# elif grade > 6 and grade <= 8:
#     print("Хорошо")
# elif grade > 8 and grade <= 10:
#     print("Отлично")
# else:
#     print("Недопустимая оценка")

# Проверка на четность и положительность:
# number = int(input("Введите число: "))
# if number % 2 == 0 and number > 0:
#     print("Число четное и положительное")
# else:
#     print("Число не соответствует требованиям")

# Проверка года на високосность
# year = int(input("Введите ЛЮБОЙ год(После рождества Христово): "))
# if year > 0 and year % 4 == 0 and year % 100 != 0:
#     print("Год високосный")
# elif year > 0 and year % 400 == 0:
#     print("Год високосный")
# else:
#     print("Год не високосный")

# Проход на американский футбол
# age = int(input("Введите возраст: "))
# health = input('''Есть ли серьезные мед.ограничения?
# Поставьте '+' или '-': ''')
# if age >= 18 and age <= 45 and health == '+':
#     print("Принято")
# else:
#     print("Отказано")

# Викторина:
# q1 = input('''Вопрос первый: В каком году началась Вторая Мировая Война?
# a)1941
# b)1914
# c)1939
# d)1945\nОтвет:''')
# q2 = input('''Вопрос второй: В каком году было Крещение Руси?
# a)1721
# b)1991
# c)1040
# d)988\nОтвет:''')
# q3 = input('''Вопрос третий: Корень из 256?
# a)15
# b)16
# c)20
# d)256\nОтвет:''')
# q4 = input('''Вопрос четвертый: Сколько будет 2+2*4?
# a)10
# b)16
# c)4
# d)11\nОтвет:''')
# q5 = input('''Вопрос пятый: Сколько лет Python?
# a)10
# b)23
# c)32
# d)15\nОтвет:''')
# if q1 == 'c)' or q1 == 'c':
#     print("Правильно!")
# else:
#     print("Неправильно, правильный ответ - c)")
#
# if q2 == 'd)' or q2 == 'd':
#     print("Правильно!")
# else:
#     print("Неправильно, правильный ответ - d)")
#
# if q3 == 'b)' or q3 == 'b':
#     print("Правильно!")
# else:
#     print("Неправильно, правильный ответ - b)")
#
# if q4 == 'a)' or q4 == 'a':
#     print("Правильно!")
# else:
#     print("Неправильно, правильный ответ - a)")
#
# if q5 == 'c)' or q5 == 'c':
#     print("Правильно!")
# else:
#     print("Неправильно, правильный ответ - c)")

# Вход на сайт:
# user = input("Введите имя пользователя: ")
# password = input("Введите пароль: ")
# if user == 'Matvey' and password == '12345':
#     print("Welcome!")
# else:
#     print("Неправильное имя или пароль")


# Калькулятор с весом и расстоянием
# weight = int(input("Введите вес(кг): "))
# dis = int(input("Введите расстояние(киллометры): "))
# if weight > 0 and weight <= 20:
#     weight2 = weight + 10
# elif weight > 20 and weight <= 50:
#     weight2 = weight + 20
# elif weight > 50 and weight <= 75:
#     weight2 = weight + 30
# elif weight > 75 and weight <= 100:
#     weight2 = weight + 40
# else:
#     print("Недопустимый вес")
#
#
# if dis > 0 and dis <= 100:
#     dis2 = dis + 25
# elif dis > 100 and dis <= 250:
#     dis2 = dis + 50
# elif dis > 250 and dis <= 500:
#     dis2 = dis + 100
# elif dis > 500 and dis <= 750:
#     dis2 = dis + 150
# else:
#     print("Недопустимая дистанция")
#
# print("Total =",(weight2),'+',(dis2),'=',(weight2+dis2),"тг")
# Хотел тут применить break, но не получилось. Устал уже, поэтому вот так