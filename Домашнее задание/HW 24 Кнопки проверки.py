# Задание №1
# import tkinter as tk
#
# def on_checkbox_toggle():
#     update_status_label()
#
# def update_status_label():
#     selected_checkboxes = [i + 1 for i in range(len(checkboxes_state)) if checkboxes_state[i].get() == 1]
#
#     status_text = "Выбраны флажки: "
#     if selected_checkboxes:
#         for i in range(len(selected_checkboxes) - 1):
#             status_text += f"{selected_checkboxes[i]}, "
#         status_text += f"{selected_checkboxes[-1]}"
#     else:
#         status_text += "Флажки не выбраны"
#     label.config(text=status_text)
#
# root = tk.Tk()
# root.title("Интерфейс")
#
# checkboxes_state = [tk.IntVar() for _ in range(3)]
#
# checkboxes = []
# for i in range(3):
#     checkbox = tk.Checkbutton(root, text="Флажок " + str(i + 1), variable=checkboxes_state[i], onvalue=1, offvalue=0, command=on_checkbox_toggle)
#     checkbox.pack(pady=5)
#     checkboxes.append(checkbox)
#
# label = tk.Label(root, text="Статус флажков:")
# label.pack(pady=10)
#
# exit_button = tk.Button(root, text="Закрыть", command=root.destroy)
# exit_button.pack(pady=10)
#
# root.mainloop()


# Задание №2
# import tkinter as tk
#
# def create_toggle_callback(group, checkbox_number):
#     def toggle():
#         on_checkbox_toggle(group, checkbox_number)
#     return toggle
#
# def on_checkbox_toggle(group, checkbox_number):
#     update_status_label(group, checkbox_number)
#
# def update_status_label(group, checkbox_number):
#     selected_checkboxes = selected_checkboxes_by_group[group]
#     if checkboxes_state[group][checkbox_number].get() == 1:
#         selected_checkboxes.add(checkbox_number + 1)
#     else:
#         selected_checkboxes.discard(checkbox_number + 1)
#
#     status_text = f"Выбраны флажки в группе {group + 1}: "
#     if selected_checkboxes:
#         first_checkbox, *rest_checkboxes = selected_checkboxes
#         status_text += str(first_checkbox)
#         for checkbox in rest_checkboxes:
#             status_text += f", {checkbox}"
#     else:
#         status_text += f"флажки не выбраны"
#     status_labels[group].config(text=status_text)
#
# root = tk.Tk()
# root.title("Интерфейс")
#
# num_groups = 2
# num_checkboxes_per_group = 3
#
# checkboxes_state = [[tk.IntVar() for _ in range(num_checkboxes_per_group)] for _ in range(num_groups)]
#
# selected_checkboxes_by_group = [set() for _ in range(num_groups)]
#
# checkboxes = []
# for group in range(num_groups):
#     checkboxes.append([])
#     for checkbox_number in range(num_checkboxes_per_group):
#         callback = create_toggle_callback(group, checkbox_number)
#         checkbox = tk.Checkbutton(root, text=f"Группа {group + 1} Флажок {checkbox_number + 1}", variable=checkboxes_state[group][checkbox_number], onvalue=1, offvalue=0, command=callback)
#         checkbox.pack(pady=5)
#         checkboxes[group].append(checkbox)
#
# status_labels = []
# for group in range(num_groups):
#     status_label = tk.Label(root, text=f"В группе {group + 1} флажки не выбраны")
#     status_label.pack(pady=5)
#     status_labels.append(status_label)
#
# exit_button = tk.Button(root, text="Закрыть", command=root.destroy)
# exit_button.pack(pady=10)
#
# root.mainloop()


# Задание №3
# import tkinter as tk
#
# class App:
#     def __init__(self, master):
#         self.master = master
#         master.title("Интерфейс")
#
#         self.checkbox_var1 = tk.IntVar()
#         self.checkbox_var2 = tk.IntVar()
#
#         self.checkbox1 = tk.Checkbutton(master, text="Опция 1", variable=self.checkbox_var1, onvalue=1, offvalue=0,command=self.update_status, bg="black", fg="white")
#         self.checkbox2 = tk.Checkbutton(master, text="Опция 2", variable=self.checkbox_var2, onvalue=1, offvalue=0,command=self.update_status, bg="black", fg="white")
#         self.status_label = tk.Label(master, text="Выберите опции и нажмите кнопку проверки", bg="black", fg="white")
#         self.check_button = tk.Button(master, text="Проверить", command=self.check_options, bg="black", fg="white")
#
#         self.checkbox1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
#         self.checkbox2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
#         self.status_label.grid(row=2, column=0, padx=10, pady=5)
#         self.check_button.grid(row=3, column=0, pady=10)
#
#     def update_status(self):
#         status_text = "Выбраны опции: "
#         if self.checkbox_var1.get() == 1:
#             status_text += "Опция 1 "
#         if self.checkbox_var2.get() == 1:
#             status_text += "Опция 2 "
#         if self.checkbox_var1.get() == 0 and self.checkbox_var2.get() == 0:
#             status_text = "Выберите опции и нажмите кнопку проверки"
#
#         self.status_label.config(text=status_text)
#
#     def check_options(self):
#         selected_options = []
#         if self.checkbox_var1.get() == 1:
#             selected_options.append("Опция 1")
#         if self.checkbox_var2.get() == 1:
#             selected_options.append("Опция 2")
#
#         if selected_options:
#             result_text = "Выбраны следующие опции: {}".format(", ".join(selected_options))
#         else:
#             result_text = "Выберите опции перед проверкой."
#
#         print(result_text)
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()