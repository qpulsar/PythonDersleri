from tkinter import *

# from tkinter.ttk import *

window = Tk()
window.title("spin")
window.geometry("300x300-10+10")

spin = Spinbox(window, from_=0, to=100, font=("Arial Bold", 30))
spin.pack()

spin1 = Spinbox(window, values=[1, 3, 6, 8, 12], font=("Arial Bold", 30))
spin1.pack()

window.mainloop()
