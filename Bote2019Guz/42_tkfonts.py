from tkinter import *
import tkinter.font

root = Tk()
root.title = "Fontlar"

fontlar = list(tkinter.font.families())
fontlar.sort()

listbox = Listbox(root, font="DejaVu 20")
listbox.pack()

for f in fontlar:
    listbox.insert(END, f)

root.mainloop()
