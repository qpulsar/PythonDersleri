from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Açılan kutu")
window.geometry("500x500-10+10")

resim = PhotoImage(file="a.png")
lbl = Label(image=resim)
lbl.pack()

window.mainloop()
