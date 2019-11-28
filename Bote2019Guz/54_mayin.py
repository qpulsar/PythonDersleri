from tkinter import *
import random

root = Tk()
root.geometry("480x440-50+50")
root.title("Mayın Tarlası v0.1")

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
lbl_sure.pack(side=LEFT, fill=Y, anchor="center")
ust.pack(side=TOP, fill=X, )
alt = Frame(root, bg="lightblue")
alt.pack(side=TOP, fill=X)
sira = 0 #hangi label
for satir in range(0, 20):
    for sutun in range(0, 20):
        lab = Label(alt, text=sira, relief = GROOVE)
        lab.grid(row=satir, column=sutun)
        sira += 1

root.mainloop()
