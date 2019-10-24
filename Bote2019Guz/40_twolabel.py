from tkinter import *

root = Tk()
root.title("Çok hızlıyım")
root.geometry("300x300-50+10")

metin1 = Label(text="Em büyük NEF")
metin1["bg"] = "#aa0055"
metin1.pack(fill=Y, expand=1)

metin2 = Label(text="En büyük BÖTE")
metin2["fg"] = "darkblue"
metin2.pack(side=LEFT)

dugme = Button(text="Kapat", command=root.quit)
dugme.pack(side=BOTTOM)

root.mainloop()
