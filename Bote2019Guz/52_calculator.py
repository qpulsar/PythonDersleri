from tkinter import *


def dugmeBas(p):
    hesapText.set(hesapText.get() + p)
    # a = int(hesapText.get())
    # hesapText.set(a)


def sil():
    hesapText.set("")


def hesapla():
    hesapText.set(str(eval(hesapText.get())))


root = Tk()
root.title("Muhteşem Calculator")
root.geometry("-50+100")

dugmeBaslik = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]

hesapText = StringVar()
font = ('digital-7', 30)
Entry(root, font=font, textvariable=hesapText, bg="SteelBlue1"). \
    grid(row=0, column=0, columnspan=5, sticky="NEWS", ipady=10)

sayac = 0
for satir in range(1, 4):
    for sutun in range(0, 3):
        Button(root, command=lambda prm=dugmeBaslik[sayac]: dugmeBas(prm),
               text=dugmeBaslik[sayac], relief=GROOVE, width=10, height=4). \
            grid(row=satir, column=sutun)
        sayac += 1
Button(root, text="0", relief=GROOVE, bg="IndianRed1", height=4,
       command=lambda: dugmeBas("0")).grid(row=4, column=0, columnspan=2, sticky="NEWS")
Button(root, text=".", relief=GROOVE, bg="IndianRed1",
       command=lambda: dugmeBas(".")).grid(row=4, column=2, sticky="NEWS")
Button(root, text="*", relief=GROOVE, bg="IndianRed1", width=10,
       command=lambda: dugmeBas("*")).grid(row=1, column=4, sticky="NEWS")
Button(root, text="/", relief=GROOVE, bg="IndianRed1",
       command=lambda: dugmeBas("/")).grid(row=2, column=4, sticky="NEWS")
Button(root, text="+", relief=GROOVE, bg="IndianRed1",
       command=lambda: dugmeBas("+")).grid(row=3, column=4, sticky="NEWS")
Button(root, text="-", relief=GROOVE, bg="IndianRed1",
       command=lambda: dugmeBas("-")).grid(row=4, column=4, sticky="NEWS")

Button(root, text="C", relief=GROOVE, bg="Red3",
       command=sil).grid(row=0, column=5, sticky="NEWS")

Button(root, text="=", relief=GROOVE, bg="lime green",
       command=hesapla).grid(row=3, column=5, rowspan=2, sticky="NEWS")

root.mainloop()
