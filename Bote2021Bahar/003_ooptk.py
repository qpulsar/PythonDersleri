import tkinter as tk


class BmPen:
    def __init__(self, p):
        print("Kurucu fonksiyon")
        p.geometry("300x300-400+100")
        p.title("OOPL")
        self.mesaj = tk.Label(p, text="Merhaba")
        self.mesaj.pack()

        buton = tk.Button(p, text="Bana tıkla", command=self.tikla)
        buton.pack()

    def tikla(self):
        print("tiklandi")
        self.mesaj["text"] = "Elveda"


pen = tk.Tk()
arayuz = BmPen(pen)
pen.mainloop()
