
import tkinter as tk
from tkinter import messagebox

def test_enter_exit(app):

    root = tk.Tk()
    root.withdraw()

    # Показываем информационное окно
    messagebox.showinfo("Информация", "Это информационное сообщение.")
