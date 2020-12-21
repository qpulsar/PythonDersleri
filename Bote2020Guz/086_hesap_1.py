from tkinter import *

root = Tk()
root.title("Hesap Makinesi")
root.geometry("300x300-50+10")


def topla():
    try:
        s3.set(int(s1.get()) + int(s2.get()))
    except:
        s3.set("Geçersiz değer!")


def cikart():
    s3.set(int(s1.get()) - int(s2.get()))


def carp():
    s3.set(int(s1.get()) * int(s2.get()))


def bol():
    s3.set(int(s1.get()) / int(s2.get()))


s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s3.set("Sonuç...")
Entry(textvariable=s1, font=("Arial", 30)).pack()
Entry(textvariable=s2, font=("Arial", 30)).pack()
Label(textvariable=s3, font=("Arial", 30)).pack()
Button(root, text="+", command=topla, font=("Arial", 30)).pack(side=LEFT)
Button(root, text="-", command=cikart, font=("Arial", 30)).pack(side=LEFT)
Button(root, text="*", command=carp, font=("Arial", 30)).pack(side=LEFT)
Button(root, text="/", command=bol, font=("Arial", 30)).pack(side=LEFT)

root.mainloop()
