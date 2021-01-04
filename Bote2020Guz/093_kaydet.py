from tkinter import *
import sqlite3


def baglanti():
    conn = sqlite3.connect("veritabani.db")
    if conn:
        print("bağlantı başarılı")
    else:
        print("Bağlantı kurulamadı")

    return conn


dbconnect = baglanti()

root = Tk()
root.title("sqlite3 browser")
root.geometry("500x500+1200+100")

Label(root, text="ID", width=10, relief=RAISED).place(x=0, y=0)
Label(root, text="İsim", width=20, relief=RAISED).place(x=80, y=0)
Label(root, text="Yaş", width=20, relief=RAISED).place(x=250, y=0)



root.mainloop()
dbconnect.close()
