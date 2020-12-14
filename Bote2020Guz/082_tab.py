from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Tab")
window.geometry("300x300-10+10")

tab_kontrol = Notebook(window)

tab1 = Frame(tab_kontrol)
tab2 = Frame(tab_kontrol)

m1 = Label(tab1, text="Çok çalışılacak")
m1.pack()

m2 = Label(tab2, text="bir hafta sonu 9 sezon dizi izlemek")
m2.pack()


tab_kontrol.add(tab1, text="Yapılacaklar")
tab_kontrol.add(tab2, text="Yapılmayacaklar")

tab_kontrol.pack(fill=BOTH, expand=True)
window.mainloop()
