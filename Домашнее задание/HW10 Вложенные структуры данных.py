# Задание №1
# genres = {
#     'Rock':[['Def Leppard'], ['Kansas'], ['Led Zeppelin']],
#     'Rap':[['FACE'], ['Snoop Dogg'], ['50 Cent']],
#     'Phonk':[['DVRST'], ['Hensonn'], ['MUPP']]
# }
# def new_value(new_key, new_values):
#     if new_key in genres:
#         genres[new_key] = new_values
#         print(f'Новый каталог жанра {new_key}: {genres[new_key]}')
# new_key = input('Введите жанр: ')
# new_values = []
# for i in range(3):
#     new_values.append([input(f'Введите новое значение {i + 1}: ')])
# new_value(new_key, new_values)

# Задание №2
# grades = {
#     'Вася':[5,5,5,4,5,4],
#     'Коля':[3,4,4,4,3,3,3],
#     'Петя':[4,4,4,4,5,3]
# }
# def find_grade(grades):
#     average_grades = {}
#     for student, student_grades in grades.items():
#         average = sum(student_grades) / len(student_grades)
#         average_grades[student] = average
#     return average_grades
# average_grades = find_grade(grades)
# for student, average in average_grades.items():
#     print(f'{student}: Средняя оценка - {average:.1f}')

# Задание №4
# authors = {
#     'Маркс':{'Капитал':'Главный труд Карла Маркса, содержащий критический анализ капитализма'
#     },
#     'Котлер':{'Основы маркетинга':'Фундаментальная книга, имеющая полное изложение о ведении маркетинга и управлении'
#     },
#     'Достоевский':{'Идиот':'Великий роман русского писателя Достоевского, написанный во время его пребывания за границей в Германии и Швейцарии'
#     }
# }
# name = input('Введите имя автора: ')
# for items in authors:
#     if name in items:
#         print(authors[name])

# Задание №5
# coordinates = (10, 15, 2)
# def sum(coords):
#     x, y, z = coords
#     return x + y + z
# result = sum(coordinates)
# print("Сумма координат:", result)