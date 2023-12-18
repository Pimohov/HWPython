# import tkinter as tk
# from tkinter import ttk
#
# class App:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Интерфейс")
#
#         self.dropdown_var = tk.StringVar()
#         self.dropdown = ttk.Combobox(root, textvariable=self.dropdown_var)
#         self.dropdown['values'] = ('Элемент 1', 'Элемент 2', 'Элемент 3')
#         self.dropdown.set('Выберите элемент')
#         self.dropdown.grid(row=0, column=0, padx=10, pady=10)
#
#         self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
#         for i in range(10):
#             self.listbox.insert(tk.END, f'Элемент {i+1}')
#         self.listbox.grid(row=1, column=0, padx=10, pady=10)
#
#         self.show_button = tk.Button(root, text="Показать выбор", command=self.show_selection)
#         self.show_button.grid(row=2, column=0, padx=10, pady=10)
#
#     def show_selection(self):
#         selected_dropdown = self.dropdown_var.get()
#         print(f"Выбранный элемент из выпадающего списка: {selected_dropdown}")
#
#         selected_items = self.listbox.curselection()
#         selected_values = [self.listbox.get(index) for index in selected_items]
#         print(f"Выбранные элементы из списка элементов: {selected_values}")
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()