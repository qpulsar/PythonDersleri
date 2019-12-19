from tkinter import *
import sqlite3


def clear():
    username.set("")
    userpass.set("")


root = Tk()
root.title("Login")
root.geometry("-50+100")

lbl_baslik = Label(root, text="LOGIN", justify=CENTER, bg="tomato")
lbl_baslik.grid(row=0, column=0, columnspan=3, sticky="NEWS")

lbl_user = Label(root, text="Kullanıcı Adı", justify=CENTER, bg="skyblue1")
lbl_user.grid(row=1, column=0, sticky="NEWS")
lbl_pass = Label(root, text="Parola", justify=CENTER, bg="skyblue1")
lbl_pass.grid(row=2, column=0, sticky="NEWS")

username = StringVar()
userpass = StringVar()

e_user = Entry(root, textvariable=username)
e_user.grid(row=1, column=1)
e_pass = Entry(root, textvariable=userpass, show='*')
e_pass.grid(row=2, column=1)

btn_clear = Button(root, text="Temizle", command=clear)
btn_clear.grid(row=3, column=0)
btn_login = Button(root, text="Giriş", command=clear)
btn_login.grid(row=3, column=1)

root.mainloop()
