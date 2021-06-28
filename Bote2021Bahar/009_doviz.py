import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *


class Cevirici:
    @staticmethod
    def dolarkactl(d):
        return d * 8.2


class Doviz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dolar - TL dönüştürücü")
        self.geometry("300x75")
        self.resizable(False, False)


class AnaFrame(ttk.Frame):
    def __init__(self, sahip):
        super().__init__(sahip)

        pad = {'padx': 5, 'pady': 5}
        self.mesaj = ttk.Label(self, text="Dolar ")
        self.mesaj.grid(column=0, row=0, sticky="W", **pad)

        self.miktar = tk.StringVar()
        self.girdi = ttk.Entry(self, textvariable=self.miktar)
        self.girdi.grid(column=1, row=0, **pad)
        self.girdi.focus()

        self.cevir = ttk.Button(self, text="Çevir")
        self.cevir['command'] = self.kactl
        self.cevir.grid(column=2, row=0, **pad)

        self.sonuc = ttk.Label(self)
        self.sonuc.grid(row=1, column=0,columnspan=3, **pad)

        self.grid(column=0, row=0, sticky="NEWS")

    def kactl(self):
        try:
            tutar = Cevirici.dolarkactl(float(self.girdi.get()))
            self.sonuc["text"] = f"{self.girdi.get()}$ {tutar}tl yapmaktadır."
        except:
            showinfo("Hata", message=ValueError)


if __name__ == '__main__':
    hesapla = Doviz()
    AnaFrame(hesapla)
    hesapla.mainloop()
