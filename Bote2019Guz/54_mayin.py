from tkinter import *
import random


def giris(olay):
    bizim_label = olay.widget  # olaya sebep olan nesne
    if bizim_label["text"] != "p":
        bizim_label["image"] = res_merak


def cikis(olay):
    bizim_label = olay.widget  # olaya sebep olan nesne
    if bizim_label["text"] != "p":
        bizim_label["image"] = res_bos


def tikla(olay):
    global kalan_mayin
    bizim_label = olay.widget  # olaya sebep olan nesne
    if bizim_label["text"] == "p":
        return
    if int(bizim_label["text"]) in mayinlar:
        bizim_label["text"] = "p"  # eğer mayın varsa içine p harfi yaz
        bizim_label["image"] = res_patla
        kalan_mayin -= 1
        lbl_kalan["text"] = kalan_mayin
    else:
        bizim_label.grid_forget()


def guncelle():
    ks = int(lbl_sure["text"])
    ks -= 1
    if ks < 1:
        lbl_sure["text"] = "Bitti"
    else:
        lbl_sure["text"] = ks
        lbl_sure.after(1000, guncelle)


root = Tk()
root.geometry("440x480-50+50")
root.title("Mayın Tarlası v0.1")
# label de kullanılacak resimleri tanımla
res_merak = PhotoImage(file="./images/nv.png")
res_bos = PhotoImage(file="./images/qm.png")
res_patla = PhotoImage(file="./images/bom.png")
# Mayınları döşe
mayinlar = []
mayin_sayisi = 50
kalan_mayin = mayin_sayisi
for i in range(0, mayin_sayisi):
    tmp = random.randrange(0, 400)
    while tmp in mayinlar:
        tmp = random.randrange(0, 400)
    mayinlar.append(tmp)

ust = Frame(root, bg='PaleTurquoise2')
lbl_kalan = Label(ust, text=kalan_mayin, width=5, height=2,
                  bg='red', fg='black',
                  font="Digital-7 20")
lbl_kalan.pack(side=LEFT, fill=Y, anchor="center")
lbl_gulen = Label(ust, text=":)", width=20, height=2,
                  bg='black', fg='red',
                  font="Digital-7 20")
lbl_gulen.pack(side=LEFT, fill=Y, anchor="center")
lbl_sure = Label(ust, text="120", width=5, height=2,
                 bg='red', fg='black',
                 font="Digital-7 20")
lbl_sure.after(1000, guncelle)
lbl_sure.pack(side=LEFT, fill=Y, anchor="center")
ust.pack(side=TOP, fill=X, )
alt = Frame(root, bg="lightblue")
alt.pack(side=TOP, fill=X)
sira = 0  # hangi label
for satir in range(0, 20):
    for sutun in range(0, 20):
        lab = Label(alt, text=sira, image=res_bos, relief=GROOVE)
        lab.grid(row=satir, column=sutun)
        lab.bind("<Enter>", giris)
        lab.bind("<Leave>", cikis)
        lab.bind("<Button-1>", tikla)
        sira += 1
root.mainloop()
