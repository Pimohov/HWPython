# Задание №1
# import tkinter as tk
#
# def label_text(label, new_text):
#     label.config(text=new_text)
#
# def button1_click():
#     label_text(label1, "Привет, User")
#
# def button2_click():
#     label_text(label2, "Кнопка нажата")
#
# root = tk.Tk()
# root.title("Интерфейс")
#
# label1 = tk.Label(root, text="Привет, это метка 1")
# label1.pack(pady=10)
#
# label2 = tk.Label(root, text="Это метка 2")
# label2.pack(pady=10)
#
# button1 = tk.Button(root, text="Изменить текст метки 1", command=button1_click)
# button1.pack(pady=10)
#
# button2 = tk.Button(root, text="Изменить текст метки 2", command=button2_click)
# button2.pack(pady=10)
#
# root.mainloop()

# Задание №2
# import tkinter as tk
#
# def add_text():
#     input_text = entry.get()
#     text_box.insert(tk.END, input_text + "\n")
#     entry.delete(0, tk.END)
#
# root = tk.Tk()
# root.title("Текстовый интерфейс")
#
# entry = tk.Entry(root, width=50)
# entry.pack(pady=10)
#
# add_button = tk.Button(root, text="Добавить", command=add_text)
# add_button.pack(pady=10)
#
# text_box = tk.Text(root, width=50, height=10)
# text_box.pack(pady=10)
#
# root.mainloop()