from tkinter import *
import sqlite3


def baglanti():
    conn = sqlite3.connect("veritabani.db")
    if conn:
        print("bağlantı başarılı")
    else:
        print("Bağlantı kurulamadı")

    return conn


def sorgu():
    sql = "select * from covid"
    cursor = dbconnect.cursor()
    cursor.execute(sql)
    sayac = 1
    while True:
        satir = cursor.fetchone()
        if satir is None:
            break
        Label(root, text=satir[0], width=10, relief=GROOVE).place(x=0, y=sayac * 22)
        Label(root, text=satir[1], width=20, relief=GROOVE).place(x=80, y=sayac * 22)
        Label(root, text=satir[2], width=20, relief=GROOVE).place(x=250, y=sayac * 22)
        sayac += 1


dbconnect = baglanti()

root = Tk()
root.title("sqlite3 browser")
root.geometry("500x500+1200+100")

Label(root, text="ID", width=10, relief=RAISED).place(x=0, y=0)
Label(root, text="İsim", width=20, relief=RAISED).place(x=80, y=0)
Label(root, text="Yaş", width=20, relief=RAISED).place(x=250, y=0)

sorgu()

root.mainloop()
dbconnect.close()
