from tkinter import *

root = Tk()
root.title("Diyalog penceresi")
root.geometry("300x300-50+10")
uyari = Label(root, text="Programdan çıkmak istediğinize emin misiniz?")
uyari.pack(side=TOP)
evet = Button(root, text="Evet", command=root.quit)
evet.pack(side=LEFT, fill=X, expand=1)
hayir = Button(root, text="Hayır")
hayir.pack(side=LEFT, fill=X, expand=1)

root.mainloop()
