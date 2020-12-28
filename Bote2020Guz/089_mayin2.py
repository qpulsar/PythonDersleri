from tkinter import *
import random


def suretut():
    global sure
    if kalan_mayin_sayisi > 0 and devam:
        sure += 1
        lbl_sure["text"] = sure
        lbl_sure.after(1000, suretut)


def uzerinde(nesne):
    bizimki = nesne.widget
    bizimki["bg"] = "violetred"


def gitti(nesne):
    bizimki = nesne.widget
    bizimki["bg"] = "dodgerblue"


def tiklandi(nesne):
    global kalan_mayin_sayisi
    bizimki = nesne.widget
    if bizimki["text"] in (".", "*"):
        return
    if int(bizimki["text"]) in mayin_tarlasi:
        print("PATLADI", bizimki["text"])
        kalan_mayin_sayisi -= 1
        lbl_mayin["text"] = kalan_mayin_sayisi
        bizimki["text"] = "*"
    else:
        bizimki["text"] = "."


mayin_sayisi = 20
kalan_mayin_sayisi = mayin_sayisi
f = ("Tahoma", 20)
sure = 0
devam = True

mayin_tarlasi = []
for i in range(mayin_sayisi):
    tmp = random.randrange(0, 400)
    while tmp in mayin_tarlasi:
        tmp = random.randrange(0, 400)

    mayin_tarlasi.append(tmp)

print(mayin_tarlasi)
root = Tk()
root.geometry("500x500+1200+100")
root.title("Mayın Tarlası v:0.2")

ust = Frame(root, bg="cadetblue")
lbl_mayin = Label(ust, text=kalan_mayin_sayisi, font=f, width=5, height=2)
lbl_mayin.grid(row=0, column=0, sticky="NWS")
Label(ust, text="", width=16, height=2, bg="cadetblue").grid(row=0, column=1)
lbl_gulen = Label(ust, text=":)", font=f, width=5, height=2)
lbl_gulen.grid(row=0, column=2)
Label(ust, text="", width=16, height=2, bg="cadetblue").grid(row=0, column=3)
lbl_sure = Label(ust, text=sure, font=f, width=5, height=2)
lbl_sure.grid(row=0, column=4, sticky="NES")
lbl_sure.after(1000, suretut)
ust.grid(row=0, column=0, sticky="NEWS")

alt = Frame(root, bg="lime")
sira = 0
for satir in range(0, 20):
    for sutun in range(0, 20):
        lbl = Label(alt, text=sira, relief=GROOVE)
        lbl.grid(row=satir, column=sutun, sticky="NEWS")
        sira += 1
        lbl.bind("<Enter>", uzerinde)
        lbl.bind("<Leave>", gitti)
        lbl.bind("<Button-1>", tiklandi)
alt.grid(row=1, column=0, sticky="NEWS")

root.mainloop()
