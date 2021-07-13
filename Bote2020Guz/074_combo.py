from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Açılan kutu")
window.geometry("300x300-10+10")

combo = Combobox(window, values=(1, 3, 6, "seçenek4", "seçenek5"))
combo.current(3)
combo.pack()

window.mainloop()
