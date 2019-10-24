from tkinter import *

root = Tk()
root.title("Diyalog penceresi")
root.geometry("800x300-50+10")

for satir in range(0,5):
    disFrame = Frame(root, borderwidth=2, bg="red")
    lbl = Label(disFrame,text="kalinlik:{}".format(satir))
    lbl.pack(side=LEFT, expand=1)
    for relief in [SOLID, SUNKEN, RAISED, FLAT, RIDGE, GROOVE]:
        icFrame=Frame(disFrame, borderwidth=satir, relief=relief)
        Button(icFrame, text=relief).pack(side=LEFT)
        icFrame.pack(side=LEFT)
    disFrame.pack()

root.mainloop()