# Задание №1, 4
# def fac(n):
#     count = 1
#     for i in range(1, n + 1):
#         count *= i
#     return count
# count = fac(5)
# print(count)

# Задание №2
# def temp(cel):
#     change = 1.8
#     zero_cel = 32
#     zero_far = 0
#     if cel > 0:
#         while zero_far != cel:
#             zero_far += 1
#             zero_cel += change
#         print(f'{cel}C = {zero_cel:.1f}F')
#     else:
#         while zero_far != cel:
#             zero_far -= 1
#             zero_cel -= change
#         print(f'{cel}C = {zero_cel:.1f}F')
# temp(-1)

# Задание №3
# def noc(x, y):
#     def nod(a, b):
#         while b != 0:
#             a, b = b, a % b
#         return a
#     return x * y // nod(x, y)
# result = noc(int(input("Введите первое число: ")), int(input("Введите второе число: ")))
# print(result)

# 5, 6 задание не получилось. Математические вычисления, не понятные в плане выражения их в виде кода

