from tkinter import *
import random

SATIR = 10
SUTUN = 10
MAYIN_SAYISI = 25
MAYIN_KOD = 9
BASILDI_KOD = 8
BULDU_KOD = 7
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


def onMouse(nesne):
    global tarla
    bizimki = nesne.widget
    info = bizimki.grid_info()
    x = info["column"]
    y = info["row"]
    if tarla[x][y] !=  BASILDI_KOD  and tarla[x][y] != BULDU_KOD:
        bizimki["image"] = res_him


def onMouseOut(nesne):
    global tarla
    bizimki = nesne.widget
    info = bizimki.grid_info()
    x = info["column"]
    y = info["row"]
    if tarla[x][y] !=  BASILDI_KOD  and tarla[x][y] != BULDU_KOD:
        bizimki["image"] = res_bos

def onClick(nesne):
    global tarla
    bizimki = nesne.widget
    info = bizimki.grid_info()
    x = info["column"]
    y = info["row"]
    if tarla[x][y]==MAYIN_KOD:
        bizimki["image"] = res_gum
        tarla[x][y] = BULDU_KOD
    else:
        bizimki["image"] = ""
        bizimki["text"]='A'
        tarla[x][y] = BASILDI_KOD


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
res_bos = PhotoImage(file="./images/bos.png")
res_him = PhotoImage(file="./images/him.png")
res_gum = PhotoImage(file="./images/gum.png")

# mayın label yerleştir
for x in range(0, SATIR):
    for y in range(0, SUTUN):
        l = Label(alt, image=res_bos, relief=SUNKEN)
        l.grid(row=x, column=y)
        # olayları kontrol et
        l.bind("<Enter>", onMouse)
        l.bind("<Leave>", onMouseOut)
        l.bind("<Button-1>", onClick)

tarla_sur()  # tarlayı 0 ile doldur
tarla_dose()  # tarlaya mayın döşe (mayın olanlara 9 koy)
tarla_bas()  # konsola yaz

pen.mainloop()
