# Задание №1
# def arithmetic_operations():
#     try:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#
#         sum_result = num1 + num2
#         difference_result = num1 - num2
#         product_result = num1 * num2
#
#         try:
#             quotient_result = num1 / num2
#             print(f"Сумма: {sum_result}")
#             print(f"Разность: {difference_result}")
#             print(f"Произведение: {product_result}")
#             print(f"Частное: {quotient_result}")
#
#         except ZeroDivisionError:
#             print("Ошибка: Деление на ноль невозможно.")
#
#     except ValueError:
#         print("Ошибка: Введите корректные числа.")
#
# arithmetic_operations()

# Задание №2
# class ValidationError(Exception):
#     pass
#
# def validate(username):
#     if not username:
#         raise ValidationError("Имя пользователя не должно быть пустым.")
#     elif not username.isalnum():
#         raise ValidationError("Имя пользователя должно состоять только из букв и цифр.")
#
# def valid():
#     while True:
#         try:
#             username = input("Введите имя пользователя: ")
#             validate(username)
#             return username
#         except ValidationError as e:
#             print(f"Ошибка валидации: {e}")
#
# try:
#     valid_username = valid()
#     print(f"Введенное имя пользователя: {valid_username}")
# except KeyboardInterrupt:
#     print("\nПрограмма завершена пользователем.")

# Задание №3
# import time
#
# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, type, value, traceback):
#         self.end_time = time.time()
#         elapsed_time = (self.end_time - self.start_time) * 1000
#         print(f"Время выполнения: {elapsed_time:.2f} миллисекунд")
#
# with Timer():
#     user_input = input("Введите что-нибудь: ")
#     print(f"Вы ввели: {user_input}")