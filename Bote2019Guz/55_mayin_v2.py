from tkinter import *
import random

SATIR = 10
SUTUN = 10
MAYIN_SAYISI = 25
MAYIN_KOD = 9
tarla = []


def tarla_sur():
    global tarla
    for sa in range(0, SATIR):
        sat = []
        for su in range(0, SUTUN):
            sat.append(0)
        tarla.append(sat)


def tarla_bas():
    global tarla
    for x in range(0, SATIR):
        for y in range(0, SUTUN):
            print("{:3}".format(tarla[x][y]), end="")
        print()

def tarla_dose():
    global tarla
    for i in range(0, MAYIN_SAYISI):
        x = random.randrange(0, SUTUN)
        y = random.randrange(0, SATIR)
        while tarla[x][y] == MAYIN_KOD:
            x = random.randrange(0, SUTUN)
            y = random.randrange(0, SATIR)
        tarla[x][y] = MAYIN_KOD

pen = Tk()
pen.title("MAYIN TARLASI v2.0")
pen.geometry("-50+100")
pen.resizable(width=False, height=False)

ust = Frame(pen)
lbl_kalan = Label(ust, text=MAYIN_SAYISI, width=4, height=2)
lbl_kalan.grid(row=0, column=0, sticky="NEWS")
lbl_gulen = Label(ust, text=":)", width=4, height=2)
lbl_gulen.grid(row=0, column=1, sticky="NEWS")
lbl_sure = Label(ust, text="120", width=4, height=2)
lbl_sure.grid(row=0, column=2, sticky="NEWS")
ust.pack(side=TOP)

alt = Frame(pen)
alt.pack(side=TOP)

#mayın label yerleştir
for x in range(0, SATIR):
    for y in range(0, SUTUN):
        l = Label(alt, image=res_bos, relief=SUNKEN)
        l.grid(row=x, column=y)
        #olayları kontrol et

tarla_sur()  #tarlayı 0 ile doldur
tarla_dose()  #tarlaya mayın döşe (mayın olanlara 9 koy)
tarla_bas()     #konsola yaz

pen.mainloop()