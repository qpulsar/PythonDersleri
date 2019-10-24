from tkinter import *
import random


def generate():
    rs = random.randint(1, 101)
    sayi["text"] = "{}".format(rs)


root = Tk()
root.title("Diyalog penceresi")
root.geometry("300x300-50+10")
sayi = Label(root, text="", font="times 30")
sayi.pack(side=TOP)
at = Button(root, text="Rastgele Sayı", command=generate)
at.pack(side=BOTTOM, expand=1)
root.mainloop()
