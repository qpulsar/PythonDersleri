from tkinter import *
from tkinter.ttk import *

sayac = 0


def arttir():
    global sayac
    sayac += 1
    bar['value'] = sayac
    if sayac < 100:
        bar.after(50, arttir)


window = Tk()
window.title("progress bar")
window.geometry("300x300-10+10")

bar = Progressbar(window, length=100)
bar['value'] = sayac
bar.pack()
bar.after(50, arttir)

stil = Style()
stil.theme_use('alt')

window.mainloop()
