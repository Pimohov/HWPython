import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(10), nullable=False)

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes")

        engine = create_engine('sqlite:///notes.db', echo=True)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

        self.create_gui()

    def create_gui(self):
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.main_frame, text="Имя пользователя:").grid(row=0, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(self.main_frame)
        self.username_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.main_frame, text="Пароль:").grid(row=1, column=0, sticky=tk.W)
        self.password_entry = ttk.Entry(self.main_frame, show='*')
        self.password_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Button(self.main_frame, text="Войти", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Регистрация", command=self.register).grid(row=3, column=0, columnspan=2, pady=10)

        self.note_tree = ttk.Treeview(self.main_frame, columns=("ID", "Название", "Создано в"))
        self.note_tree.heading("ID", text="ID")
        self.note_tree.heading("Название", text="Название")
        self.note_tree.heading("Создано в", text="Создано в")
        self.note_tree.grid(row=4, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        ttk.Button(self.main_frame, text="Добавить заметку", command=self.add_note).grid(row=5, column=0, pady=5)
        ttk.Button(self.main_frame, text="Редактировать заметку", command=self.edit_note).grid(row=5, column=1, pady=5)
        ttk.Button(self.main_frame, text="Удалить заметку", command=self.delete_note).grid(row=6, column=0, columnspan=2, pady=5)

        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.session.query(User).filter_by(username=username, password=password).first()
        if user:
            self.load_notes()
        else:
            messagebox.showerror("Ошибка", "Неправильное имя пользователя или пароль")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Ошибка", "Оба поля пустые")
            return

        existing_user = self.session.query(User).filter_by(username=username).first()
        if existing_user:
            messagebox.showerror("Ошибка", "Имя уже занято. Пожалуйста выберите другое.")
            return

        new_user = User(username=username, password=password)
        self.session.add(new_user)
        self.session.commit()

        messagebox.showinfo("Успешно!", "Регистрация успешна! Вы можете войти.")

    def load_notes(self):
        for item in self.note_tree.get_children():
            self.note_tree.delete(item)

        username = self.username_entry.get()
        user = self.session.query(User).filter_by(username=username).first()
        if user:
            notes = self.session.query(Note).filter_by(user_id=user.id).all()
            for note in notes:
                self.note_tree.insert("", "end", values=(note.id, note.title, note.created_at))

    def add_note(self):
        title = simpledialog.askstring("Добавить заметку", "Введите название заметки:")
        content = simpledialog.askstring("Добавить заметку", "Введите содержание заметки:")

        if title and content:
            new_note = Note(title=title, content=content, user_id=1)
            self.session.add(new_note)
            self.session.commit()
            self.load_notes()

    def edit_note(self):
        selected_item = self.note_tree.selection()
        if not selected_item:
            messagebox.showwarning("Внимание", "Выберите заметку для изменения.")
            return

        note_id = self.note_tree.item(selected_item, "values")[0]
        note = self.session.query(Note).filter_by(id=note_id).first()

        if not note:
            messagebox.showerror("Ошибка", "Заметка не выбрана.")
            return

        new_title = simpledialog.askstring("Редактировать", "Редактировать название заметки:", initialvalue=note.title)
        new_content = simpledialog.askstring("Редактировать", "Редактировать содеражние заметки:", initialvalue=note.content)

        if new_title is not None and new_content is not None:
            note.title = new_title
            note.content = new_content
            self.session.commit()
            self.load_notes()

    def delete_note(self):
        selected_item = self.note_tree.selection()
        if not selected_item:
            messagebox.showwarning("Внимание", "Выберите заметку для удаления.")
            return

        confirmation = messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить эту заметку?")
        if confirmation:
            note_id = self.note_tree.item(selected_item, "values")[0]
            note = self.session.query(Note).filter_by(id=note_id).first()

            if note:
                self.session.delete(note)
                self.session.commit()
                self.load_notes()
                messagebox.showinfo("Успешно", "Заметка успешно удалена.")
            else:
                messagebox.showerror("Ошибка", "Заметка не найдена.")


if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
