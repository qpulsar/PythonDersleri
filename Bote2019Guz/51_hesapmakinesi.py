from tkinter import *


def dugmeBas(ad):
    bagkur.set(bagkur.get() +str(ad))


root = Tk()
root.title("Hesap makinesi")
root.geometry("-50+100")

dugmeler = [7, 8, 9, 4, 5, 6, 1, 2, 3]
sayac = 0
for satir in range(1, 4):
    for sutun in range(0, 3):
        Button(root, text=str(dugmeler[sayac]), command=lambda p=dugmeler[sayac]:dugmeBas(p),
               relief=GROOVE, width=10, height=4). \
            grid(row=satir, column=sutun)
        sayac += 1
bagkur = StringVar()
Entry(root, textvariable=bagkur).grid(row=0, column=0, columnspan=3,
                                      sticky="NEWS")
Button(root, text="0", relief=GROOVE, width=10, height=4, bg="powder blue"). \
    grid(row=4, column=0, columnspan=2, sticky="NEWS")
Button(root, text=".", relief=GROOVE, width=10, height=4, bg="tomato"). \
    grid(row=4, column=2, sticky="NEWS")
Button(root, text="*", relief=GROOVE, width=10, height=4, bg="SpringGreen"). \
    grid(row=0, column=3, sticky="NEWS")
Button(root, text="/", relief=GROOVE, width=10, height=4, bg="SpringGreen"). \
    grid(row=1, column=3, sticky="NEWS")
Button(root, text="+", relief=GROOVE, width=10, height=4, bg="SpringGreen"). \
    grid(row=2, column=3, sticky="NEWS")
Button(root, text="-", relief=GROOVE, width=10, height=4, bg="SpringGreen"). \
    grid(row=3, column=3, sticky="NEWS")
Button(root, text="=", relief=GROOVE, width=10, height=4, bg="Red"). \
    grid(row=4, column=3, sticky="NEWS")

root.mainloop()
