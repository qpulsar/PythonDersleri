from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

window = Tk()
window.title("Dialog penceresi")
window.geometry("300x300-10+10")

file = filedialog.askdirectory()
print(file)

dosyalar = filedialog.askopenfilenames()
print(dosyalar)

window.mainloop()
