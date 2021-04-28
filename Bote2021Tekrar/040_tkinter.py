from tkinter import *

pencere = Tk()
pencere.title("Merhaba Dünya")
pencere.geometry("400x500-1+0")
pencere.resizable(width=False, height=False)

lbl = Label(pencere, text="Merhaba Böte 50", font=("Arial", 40),
            bg="lime")
lbl["fg"] = "MediumPurple3"
lbl.pack()
pencere.mainloop()
