from tkinter import *

def konus():
    metin["text"] = "Merhaba Gülüm"

root = Tk()
root.geometry("300x300-50+10")

metin = Label(text="", font="digital-7 20")
metin.pack()

dugme = Button(text="Merhaba De", command=konus)
dugme.pack()

root.mainloop()
