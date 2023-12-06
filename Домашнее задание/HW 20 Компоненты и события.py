# Задание №1
# import tkinter as tk
#
# def button_click():
#     label.config(text="Текст изменен")
#
# root = tk.Tk()
# root.title("Мой интерфейс")
#
# label = tk.Label(root, text="Нажмите кнопку для изменения текста")
# label.pack()
#
# button = tk.Button(root, text="Изменить текст", command=button_click)
# button.pack()
#
# root.mainloop()

# Задание №2
# import tkinter as tk
#
# def clear_text():
#     entry.delete(0, tk.END)
#
# def process_text():
#     text = entry.get()
#     print(f"Текст: {text}")
#
# def on_enter_pressed(event):
#     process_text()
#
# root = tk.Tk()
# root.title("Мой интерфейс")
#
# entry = tk.Entry(root, width=30)
# entry.pack()
#
# clear_button = tk.Button(root, text="Очистить", command=clear_text)
# clear_button.pack()
#
# process_button = tk.Button(root, text="Выполнить", command=process_text)
# process_button.pack()
#
# root.bind('<Return>', on_enter_pressed)
#
# root.mainloop()