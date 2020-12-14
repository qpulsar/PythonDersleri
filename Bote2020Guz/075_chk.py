from tkinter import *
from tkinter.ttk import *

def bak():
    print(kontrol.get())

window = Tk()
window.title("Check")
window.geometry("300x300-10+10")

kontrol = BooleanVar()
kontrol.set(True)
chk = Checkbutton(window,text="Olsun mu?", var=kontrol)
chk.pack()

btn = Button(window,text="Bak bakalım",command=bak)
btn.pack()

window.mainloop()
