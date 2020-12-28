from tkinter import *


def fare_geldi(w):
    e = w.widget
    e["text"] = "A"
    e["bg"] = "darkorange"


def fare_gitti(w):
    e = w.widget
    e["text"] = "*"
    e["bg"] = "lightblue"


def fare_tik(w):
    e = w.widget
    e["text"] = "O"
    e["bg"] = "lightcoral"

def zamanilerle():
    suretut.set(suretut.get() + 1)
    sure.after(1000, zamanilerle)


root = Tk()
root.title("Mayın Tarlası 0.1")
root.geometry("500x500")
# Üst frame

kalanmayin = IntVar()
kalanmayin.set(20)
suretut = IntVar()
suretut.set(0)

ust = Frame(root, bg="darksalmon")
sure = Label(ust, textvariable=suretut, font=("Tahoma", 20), width=10, height=2, bg="Springgreen", fg="gray50")
sure.pack(fill=Y, anchor=CENTER, side=RIGHT)
sure.after(1000, zamanilerle)
kalan = Label(ust, textvariable=kalanmayin, font=("Tahoma", 20), width=10, height=2, bg="wheat1")
kalan.pack(fill=Y, anchor=CENTER, side=LEFT)
ust.pack(fill=X, side=TOP)

# Mayın tarlasın
alt = Frame(root, bg="darksalmon")
for i in range(0, 10):
    for j in range(0, 10):
        lbl = Label(alt, text="*", relief=SUNKEN, width=6, height=2)
        lbl.grid(row=i, column=j)
        lbl.bind("<Enter>", fare_geldi)
        lbl.bind("<Leave>", fare_gitti)
        lbl.bind("<Button-1>", fare_tik)

alt.pack(fill=BOTH, expand=True, side=BOTTOM)
root.mainloop()
