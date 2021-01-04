from tkinter import *
import sqlite3


def baglanti():
    global conn
    conn = sqlite3.connect("veritabani.db")
    if conn:
        print("bağlantı başarılı")
    else:
        print("Bağlantı kurulamadı")


def temizle():
    isim.set("")
    yas.set(0)

def kaydet():
    global conn
    sql = "insert into covid(isim, yas) values('{}',{})".format(isim.get(), yas.get())
    c = conn.cursor()
    c.execute(sql)
    conn.commit()


root = Tk()
root.title("sqlite3 browser")
root.geometry("500x500+1200+100")

isim = StringVar()
yas = IntVar()

Label(root, text="SQLite3 Kayıt Örneği", bg="lightcoral", font="verdana 20", anchor=CENTER). \
    grid(column=0, row=0, columnspan=3, sticky="EW")
Label(root, text="İsim", width=20, relief=RAISED).grid(column=0, row=1, pady=5)
Label(root, text="Yaş", width=20, relief=RAISED).grid(column=0, row=2)
Entry(root, textvariable=isim, width=30).grid(column=1, row=1)
Entry(root, textvariable=yas, width=30).grid(column=1, row=2)
Button(root, text="Bağlan", bg="green", command=baglanti).grid(column=3, row=0, rowspan=3, sticky="NEWS")
Button(root, text="Kaydet", command=kaydet, bg="lightblue").grid(column=0, row=3, columnspan=3)
Button(root, text="Temizle", command=temizle, bg="gray30").grid(column=0, row=3)

root.mainloop()
conn.close()
