from tkinter import *

f = ("Arial", 20)
root = Tk()
root.title("Advanced Calculator")
root.geometry("+1200+10")


def temizle():
    global noktavar
    sayi.set("")
    noktavar = False


def sayiekle(dugme):
    sayi.set(sayi.get() + str(dugme))


def nokta():
    global noktavar
    if not noktavar:
        sayi.set(sayi.get() + ".")
        noktavar = True


def islem(isaret):
    global noktavar
    sayi.set(sayi.get() + isaret)
    noktavar = False


def hesapla():
    sayi.set(eval(sayi.get()))


noktavar = False
sayi = StringVar()

dizilis = [7, 8, 9, 4, 5, 6, 1, 2, 3]
Entry(root, textvariable=sayi, font=f).grid(row=0, column=0, columnspan=3)
sayac = 0
for satir in range(1, 4):
    for sutun in range(0, 3):
        Button(root, text=dizilis[sayac], width=4, height=2, font=f,
               command=lambda p=dizilis[sayac]: sayiekle(p)) \
            .grid(row=satir, column=sutun, sticky="NEWS")
        sayac += 1
Button(root, text="0", width=4, height=2, font=f,
       command=lambda p=0: sayiekle(p)). \
    grid(row=4, column=0, sticky="NEWS", columnspan=2)
Button(root, text=".", width=4, height=2, font=f, command=nokta). \
    grid(row=4, column=2, sticky="NEWS")
Button(root, text="C", width=2, height=1, font=f, bg="gray30", command=temizle). \
    grid(row=0, column=3)
Button(root, text="/", width=2, height=2, font=f, bg="IndianRed1", command=lambda z="/": islem(z)). \
    grid(row=1, column=3)
Button(root, text="*", width=2, height=2, font=f, bg="IndianRed1", command=lambda z="*": islem(z)). \
    grid(row=2, column=3)
Button(root, text="-", width=2, height=2, font=f, bg="IndianRed1", command=lambda z="-": islem(z)). \
    grid(row=3, column=3)
Button(root, text="+", width=2, height=2, font=f, bg="IndianRed1", command=lambda z="+": islem(z)). \
    grid(row=4, column=3)
Button(root, text="=", width=2, height=2, font=f, bg="red2", command=hesapla). \
    grid(row=5, column=0, columnspan=4, sticky="NEWS")

root.mainloop()
