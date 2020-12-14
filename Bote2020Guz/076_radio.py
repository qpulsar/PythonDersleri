from tkinter import *


def secim():
    lbl.config(text=hangisi.get())
    if hangisi.get() == 1:
        lbl["font"] = ("Arial", 30)
        lbl["bg"] = "sandy brown"


window = Tk()
window.title("Radio")
window.geometry("300x300-10+10")
hangisi = IntVar()
r1 = Radiobutton(window, text="BÖTE", value=1, var=hangisi)
r2 = Radiobutton(window, text="Fen", value=2, var=hangisi)
r3 = Radiobutton(window, text="Sınıf", value=3, var=hangisi)
r4 = Radiobutton(window, text="Fizik", value=4, var=hangisi)
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
r4.pack(side=LEFT)

lbl = Label(window, text="Seçiminiz...", bg="red")
lbl.pack(side=BOTTOM)

btn = Button(window, text="Seçin ve Tıklayın", command=secim)
btn.pack(side=BOTTOM)

window.mainloop()
