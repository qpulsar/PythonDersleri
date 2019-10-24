from tkinter import *

root = Tk()
root.title("Diyalog penceresi")
root.geometry("300x300-50+10")
alan1 = Frame(root, borderwidth=2, relief=SUNKEN,bg="yellow")
metin1 = Label(alan1, text="Alan 1'in içi")
metin1.pack()
alan1.pack(fill=X, expand=1)
alan2 = Frame(root, borderwidth=2, relief=RAISED, bg="darkblue")
metin2 = Label(alan2, text="Alan 2'in içi")
metin2.pack()
alan2.pack(fill=Y, expand=1)
root.mainloop()