from tkinter import *

root = Tk()
root.geometry("+1200+100")
root.title("Login")


def check():
    if un.get() == "admin" and pw.get() == "123":
        print("Giriş başarılı")
    else:
        print("Hata var!")


def clear():
    un.set("")
    pw.set("")


f = ("Verdana", 20)
un = StringVar()
pw = StringVar()
Label(root, text="Username", font=f).grid(row=0, column=0)
Label(root, text="password", font=f).grid(row=1, column=0)
Entry(root, textvariable=un, font=f).grid(row=0, column=1)
Entry(root, textvariable=pw, font=f, show="*").grid(row=1, column=1)
Button(root, text="OK", command=check, font=f).grid(row=2, column=0, columnspan=2)
Button(root, text="Clear", command=clear, font=f).grid(row=2, column=0)
img = PhotoImage(file="user.png")
lbl = Label(root, image=img)
lbl.grid(row=0, column=2, rowspan=3)
lbl["image"] = img

root.mainloop()
