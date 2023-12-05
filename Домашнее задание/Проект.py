# import json
# import os
#
# class Task:
#     def __init__(self, title, description, deadline):
#         self.title = title
#         self.description = description
#         self.deadline = deadline
#
#     def __str__(self):
#         return f"Название: {self.title}\nОписание: {self.description}\nДата: {self.deadline}"
#
# class ToDoList:
#     def __init__(self, filename="tasks.json"):
#         self.filename = filename
#         self.tasks = self.load_tasks()
#
#     def load_tasks(self):
#         if os.path.exists(self.filename):
#             with open(self.filename, 'r') as file:
#                 tasks_data = json.load(file)
#                 return [Task(**task_data) for task_data in tasks_data]
#         else:
#             return []
#
#     def save_tasks(self):
#         tasks_data = [{"название": task.title, "описание": task.description, "дата": task.deadline} for task in self.tasks]
#         with open(self.filename, 'w') as file:
#             json.dump(tasks_data, file, indent=2)
#
#     def add_task(self, title, description, deadline):
#         task = Task(title, description, deadline)
#         self.tasks.append(task)
#         self.save_tasks()
#
#     def view_tasks(self):
#         for index, task in enumerate(self.tasks, 1):
#             print(f"\nЗадача {index}:\n{task}")
#
#     def edit_task(self, index, title, description, deadline):
#         if 1 <= index <= len(self.tasks):
#             task = self.tasks[index - 1]
#             task.title = title
#             task.description = description
#             task.deadline = deadline
#             self.save_tasks()
#         else:
#             print("Неправильный индекс задачи")
#
#     def delete_task(self, index):
#         if 1 <= index <= len(self.tasks):
#             del self.tasks[index - 1]
#             self.save_tasks()
#         else:
#             print("Неправильный индекс задачи")
#
# def main():
#     todo_list = ToDoList()
#
#     while True:
#         print("\nМеню:")
#         print("1. Добавить задачу")
#         print("2. Посмотреть задачи")
#         print("3. Редактировать задачу")
#         print("4. Удалить задачу")
#         print("0. Выход")
#
#         choice = input("Выбор: ")
#
#         if choice == "0":
#             break
#         elif choice == "1":
#             title = input("Введите название задачи: ")
#             description = input("Введите описание задачи: ")
#             deadline = input("Введите дату задачи(ГГГГ-ММ-ДД): ")
#             todo_list.add_task(title, description, deadline)
#         elif choice == "2":
#             todo_list.view_tasks()
#         elif choice == "3":
#             index = int(input("Введите индекс задачи для редактирования: "))
#             title = input("Введите новое название задачи: ")
#             description = input("Введите новое описание задачи: ")
#             deadline = input("Введите новую дату задачи(ГГГГ-ММ-ДД): ")
#             todo_list.edit_task(index, title, description, deadline)
#         elif choice == "4":
#             index = int(input("Введите индекс задачи для удаления: "))
#             todo_list.delete_task(index)
#         else:
#             print("Ошибка выбора. Попробуйте ещё раз")
#
# if __name__ == "__main__":
#     main()