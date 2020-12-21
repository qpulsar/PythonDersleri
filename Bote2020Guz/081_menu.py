from tkinter import *


def yeni():
    print("Yeni dosya işlemleri")


window = Tk()
window.title("Menü")
window.geometry("300x300-10+10")

menu = Menu(window)
madde = Menu(menu, tearoff=False)
madde.add_command(label="Yeni Dosya", command=yeni)
madde.add_command(label="Aç...")
madde.add_command(label="Sil")

edit = Menu(window)
edit.add_command(label="Kopyala")
edit.add_command(label="Yapıştır")
edit.add_command(label="Kes")

madde.add_cascade(label="Düzenle", menu=edit)

menu.add_cascade(label="Dosya", menu=madde)

window.config(menu=menu)
window.mainloop()
