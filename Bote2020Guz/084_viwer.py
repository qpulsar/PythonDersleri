from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

window = Tk()
window.title("Açılan kutu")
window.geometry("600x600-10+10")


def yukle():
    dosya = filedialog.askopenfilename()
    print(dosya)
    resim = PhotoImage(file=dosya)
    lbl["image"] = resim
    lbl.image = resim


btn = Button(text="Resim Yükle", command=yukle)
btn.pack()

resim = PhotoImage(file="a.png")
lbl = Label(image=resim)
lbl.pack(side=BOTTOM, fill=BOTH, expand=YES)

window.mainloop()
