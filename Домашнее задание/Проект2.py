import tkinter as tk

def window():
    new_win = tk.Tk()
    new_win.title("Paint")
    new_win.geometry('700x500')

    # Дефы
    def exit_button():
        new_win.destroy()
        win.destroy()

    def new_file_button():
        new_win.destroy()
        window()

    def draw_coord(event):
        canvas.create_line(event.x, event.y, event.x, event.y)
        canvas.old_coords = event.x, event.y

    def draw(event):
        x, y = event.x, event.y
        canvas.create_line(canvas.old_coords[0], canvas.old_coords[1], x, y, width=2, fill='black')
        canvas.old_coords = x, y

    # Кнопочки
    new_file = tk.Button(new_win, text="Новый файл", command=new_file_button, bg='white', fg='black', width=10)
    new_file.place(x=0, y=0)
    exit = tk.Button(new_win, text="Выход", command=exit_button, bg='black', fg='white', width=10)
    exit.place(x=620, y=0)

    # Метка
    paint = tk.Label(new_win, text="Paint", font='CutOutOFFont', bg='red', fg='white', width=44)
    paint.place(x=83, y=0)

    # Холст
    canvas = tk.Canvas(new_win, height=800, width=600, bg='white')
    canvas.place(x=80, y=25)
    canvas.last = None
    canvas.bind('<B1-Motion>', draw)
    canvas.bind('<Button-1>', draw_coord)

    # Фреймы
    ff = tk.Frame(new_win, height=700, width=80, bg='aquamarine')
    ff.place(x=0, y=26)
    sf = tk.Frame(new_win, height=700, width=80, bg='aquamarine')
    sf.place(x=620, y=26)

    new_win.mainloop()

# Нач.окно
win = tk.Tk()
win.title("Paint")
win.geometry('300x120')
def enter(event):
    new_file.invoke()

file = tk.Label(win, text="Добро пожаловать в Paint! \nСоздайте файл:", pady=10, font='CutOutOFFont')
file.pack()
new_file = tk.Button(win, text="Новый файл", command=window, bg='red', fg='white', width=10, height=5, font='CutOutOFFont')
new_file.pack()
win.bind('<Return>', enter)

win.mainloop()
