from tkinter import *


def tiklaninca():
    lbl["text"] = txt.get()


window = Tk()
window.title("Metin Gir")
window.geometry("300x300-10+10")

lbl = Label(window, text="***", font=("Arial", 50))
lbl.pack()

txt = Entry(window, width=20, font=("Comic Sans MS", 20))
txt.pack()

btn = Button(window, text="Beni Tıkla", command=tiklaninca)
btn.pack()
window.mainloop()
