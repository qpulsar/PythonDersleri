from tkinter import *

def topla():
    sayi1 = int(s1.get())
    sayi2 = int(s2.get())
    hesap.set("{}".format(sayi1+sayi2))

root = Tk()
root.title("Diyalog penceresi")
root.geometry("300x300-50+10")
s1 = Entry()
s1.pack()
s2 = Entry()
s2.pack()
but = Button(text="+", command=topla)
but.pack()
hesap=StringVar()
sonuc = Label(text="", textvariable=hesap)
sonuc.pack()
root.mainloop()