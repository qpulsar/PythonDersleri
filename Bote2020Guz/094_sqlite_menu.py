from tkinter import *
import sqlite3


def baglanti():
    global conn
    global baglanButon

    if baglanButon["text"] == "Bağlan":
        conn = sqlite3.connect(vt_adi.get())
        if conn:
            print("bağlantı başarılı")
            baglanButon["text"] = "Bağlantıyı kes"
        else:
            print("Bağlantı kurulamadı")
            baglanButon["text"] = "Bağlan"
    elif baglanButon["text"] == "Bağlantıyı kes":
        conn.close()
        baglanButon["text"] = "Bağlan"


def vtFrameHazirla():
    global vtFrame
    global baglanButon
    Label(vtFrame, text="VT Bağlantısı", font=fontBaslik, width=20).grid(column=0, row=0, columnspan=2, pady=5,
                                                                         sticky="NEWS")
    Label(vtFrame, text="VT Adı", font=fontLabel).grid(column=0, row=1, sticky="NEWS")
    Entry(vtFrame, textvariable=vt_adi, font=fontLabel).grid(column=1, row=1)
    baglanButon = Button(vtFrame, text="Bağlan", font=fontLabel, command=baglanti)
    baglanButon.grid(column=0, row=2, pady=20, columnspan=2)


def temizle():
    isim.set("")
    yas.set(0)


def kaydet():
    global conn
    if conn is None:
        print("bağlanda gel")
        vtbaglan()

    sql = "insert into covid(isim, yas) values('{}',{})".format(isim.get(), yas.get())
    c = conn.cursor()
    c.execute(sql)
    conn.commit()


def keFrameHazirla():
    global vtFrame
    Label(keFrame, text="Kayıt Ekle", font=fontBaslik).grid(column=0, row=0, columnspan=3, pady=5,
                                                            sticky="NEWS")
    Label(keFrame, text="İsim", width=20, relief=RAISED).grid(column=0, row=1, pady=5)
    Label(keFrame, text="Yaş", width=20, relief=RAISED).grid(column=0, row=2)
    Entry(keFrame, textvariable=isim, width=30).grid(column=1, row=1)
    Entry(keFrame, textvariable=yas, width=30).grid(column=1, row=2)
    Button(keFrame, text="Bağlan", bg="green", command=baglanti).grid(column=3, row=0, rowspan=3, sticky="NEWS")
    Button(keFrame, text="Kaydet", command=kaydet, bg="lightblue").grid(column=0, row=3, columnspan=3)
    Button(keFrame, text="Temizle", command=temizle, bg="gray30").grid(column=0, row=3)


def lsFrameHazirla():
    global vtFrame
    global conn
    Label(lsFrame, text="Listele", font=fontBaslik).grid(column=0, row=0, columnspan=3, pady=5,
                                                         sticky="NEWS")
    Label(lsFrame, text="ID", width=10, relief=RAISED).grid(column=0, row=1)
    Label(lsFrame, text="İsim", width=20, relief=RAISED).grid(column=1, row=1)
    Label(lsFrame, text="Yaş", width=20, relief=RAISED).grid(column=2, row=1)

    sql = "select * from covid"
    cursor = conn.cursor()
    cursor.execute(sql)
    sayac = 2
    while True:
        satir = cursor.fetchone()
        if satir is None:
            break
        Label(lsFrame, text=satir[0], width=10, relief=GROOVE).grid(column=0, row=sayac)
        Label(lsFrame, text=satir[1], width=20, relief=GROOVE).grid(column=1, row=sayac)
        Label(lsFrame, text=satir[2], width=20, relief=GROOVE).grid(column=2, row=sayac)
        sayac += 1


def unut(kimi):
    for kim in kimi:
        if kim is not None:
            kim.forget()


def vtbaglan():
    print("Yeni vt işlemleri")
    global vtFrame
    global keFrame
    global lsFrame
    unut([keFrame, lsFrame])

    if vtFrame is not None:
        vtFrame.pack(fill=BOTH, expand=True)
    else:
        vtFrame = Frame(window, bg="lime")
        vtFrame.pack(fill=BOTH, expand=True)
        vtFrameHazirla()


def kayitekle():
    print("Kayıt Ekleme")
    global vtFrame
    global keFrame
    global lsFrame

    unut([vtFrame, lsFrame])

    if keFrame is not None:
        keFrame.pack(fill=BOTH, expand=True)
    else:
        keFrame = Frame(window, bg="blue")
        keFrame.pack(fill=BOTH, expand=True)
        keFrameHazirla()


def listele():
    print("Kayıtları Listele")
    global vtFrame
    global keFrame
    global lsFrame
    unut([vtFrame, keFrame])

    if lsFrame is not None:
        lsFrame.pack(fill=BOTH, expand=True)
    else:
        lsFrame = Frame(window, bg="orange")
        lsFrame.pack(fill=BOTH, expand=True)
        lsFrameHazirla()


lsFrame = None
keFrame = None
vtFrame = None

window = Tk()
window.title("Menü")
window.geometry("300x300-10+10")

vt_adi = StringVar()
vt_adi.set("veritabani.db")
isim = StringVar()
yas = IntVar()
conn = None
fontBaslik = ("Verdana", 20)
fontLabel = ("Arial", 16)
menu = Menu(window)
madde = Menu(menu, tearoff=False)
madde.add_command(label="Veri Tabanı Bağlantısı", command=vtbaglan)
madde.add_command(label="Kayıt Ekle", command=kayitekle)
madde.add_command(label="Kayıtları Listele", command=listele)

menu.add_cascade(label="Veri Tabanı İşlemleri", menu=madde)

window.config(menu=menu)
window.mainloop()
