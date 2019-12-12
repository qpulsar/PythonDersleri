from tkinter import *
import random

# SABİTLER
SATIR = 10
SUTUN = 10
MAYIN_SAYISI = 25
# Matriste yer alan sayıların anlamları
KOD_MAYIN = 9  # Tarlada gömülü mayın
KOD_PATLADI = 8  # Mayın vardı biz basdık patladı
KOD_BOS = 0  # Tarlanın boş bir yeri
KOD_BOSTU = 7  # Biz tıkladık açtık ama boşmuş
tarla = []
sure = 0  # kronometre


def tarla_hazirla():
    global tarla
    for satir in range(0, SATIR):
        satmat = []
        for sutun in range(0, SUTUN):
            satmat.append(KOD_BOS)
        tarla.append(satmat)


def tarla_ekrana_yaz():
    global tarla
    for satir in range(0, SATIR):
        for sutun in range(0, SUTUN):
            print("{:2}".format(tarla[satir][sutun]), end="")
        print()


def mayin_dose():
    global tarla
    for i in range(0, MAYIN_SAYISI):
        sat = random.randrange(0, SATIR)
        sut = random.randrange(0, SUTUN)
        while tarla[sat][sut] == KOD_MAYIN:
            sat = random.randrange(0, SATIR)
            sut = random.randrange(0, SUTUN)

        tarla[sat][sut] = KOD_MAYIN


def onMouseOver(nesne):
    global tarla
    lab = nesne.widget
    koordinat = lab.grid_info()
    sat, sut = koordinat["row"], koordinat["column"]
    if tarla[sat][sut] not in [KOD_BOSTU, KOD_PATLADI]:
        lab["image"] = img_mrk


def onMouseOut(nesne):
    global tarla
    lab = nesne.widget
    koordinat = lab.grid_info()
    sat, sut = koordinat["row"], koordinat["column"]
    if tarla[sat][sut] not in [KOD_BOSTU, KOD_PATLADI]:
        lab["image"] = img_bos


def onClick(nesne):
    global tarla
    global kalanMayin
    lab = nesne.widget
    koordinat = lab.grid_info()
    sat, sut = koordinat["row"], koordinat["column"]
    if tarla[sat][sut] == KOD_PATLADI:
        return
    if tarla[sat][sut] == KOD_MAYIN:
        lab["image"] = img_bam
        tarla[sat][sut] = KOD_PATLADI
        kalanMayin -= 1
        lbl_kalan["text"] = kalanMayin
    else:
        lab["image"] = ""
        tarla[sat][sut] = KOD_BOSTU


def zaman():
    global sure
    sure += 1
    lbl_sure["text"] = sure
    lbl_sure.after(1000, zaman)


if __name__ == '__main__':
    tarla_hazirla()
    mayin_dose()
    tarla_ekrana_yaz()

    pen = Tk()
    pen.title("Mayın Tarlası *Forever*")
    pen.geometry("-100+100")
    pen.resizable(width=False, height=False)

    kalanMayin = MAYIN_SAYISI
    ust = Frame(pen)
    lbl_sure = Label(ust, text="0", width=4, height=2)
    lbl_sure.grid(row=0, column=0, sticky="NEWS")
    lbl_sure.after(1000, zaman)
    lbl_durum = Label(ust, text=":)", width=4, height=2)
    lbl_durum.grid(row=0, column=1, sticky="NEWS")
    lbl_kalan = Label(ust, text=kalanMayin, width=4, height=2)
    lbl_kalan.grid(row=0, column=2, sticky="NEWS")
    ust.pack(side=TOP)

    img_bos = PhotoImage(file="./images/bos.png")
    img_mrk = PhotoImage(file="./images/him.png")
    img_bam = PhotoImage(file="./images/gum.png")

    alt = Frame(pen)
    for sat in range(0, SATIR):
        for sut in range(0, SUTUN):
            l = Label(alt, image=img_bos, relief=GROOVE)
            l.grid(row=sat, column=sut)
            # olaylar olaylar...
            l.bind("<Enter>", onMouseOver)
            l.bind("<Leave>", onMouseOut)
            l.bind("<Button-1>", onClick)

    alt.pack(side=TOP)

    pen.mainloop()
