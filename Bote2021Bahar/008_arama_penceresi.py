import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):  # constructor - kurucu
        super().__init__()
        self.title("Bul değiştir")
        self.geometry("400x150+1400+150")
        self.resizable(False, False)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        # içindekileri oluştur
        self.icini_olustur()

    def icini_olustur(self):
        giris_frame = GirisFrame(self)
        giris_frame.grid(column=0, row=0, sticky="WE")
        dugme_frame = DugmeFrame(self)
        dugme_frame.grid(column=1, row=0)


class GirisFrame(ttk.Frame):
    def __init__(self, sahip):
        super().__init__(sahip)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        ttk.Label(self, text="Aranan ifade").grid(column=0, row=0, sticky="W")
        ara = ttk.Entry(self, width=25)
        ara.focus()
        ara.grid(column=1, row=0, sticky="W")

        ttk.Label(self, text="Değiştir").grid(column=0, row=1, sticky="W")
        degis = ttk.Entry(self, width=25)
        degis.grid(column=1, row=1, sticky="W")

        # checkbox
        harf = ttk.Checkbutton(self, text="Büyük küçük harfe duyarlı")
        harf.grid(column=0, row=2, columnspan=2, sticky="W")

        tam = ttk.Checkbutton(self, text="Yalnız tam kelime ara")
        tam.grid(column=0, row=3, columnspan=2, sticky="W")

        # frame'in bütün elemanlarını alan döngü
        for b in self.winfo_children():
            b.grid(padx=1, pady=4)


class DugmeFrame(ttk.Frame):
    def __init__(self, sahip):
        super().__init__(sahip)
        self.columnconfigure(0, weight=1)
        ttk.Button(self, text="Sonrakini Bul").grid(column=0, row=0)
        ttk.Button(self, text="Değiştir").grid(column=0, row=1)
        ttk.Button(self, text="Hepsini Değiştir").grid(column=0, row=2)
        ttk.Button(self, text="İptal").grid(column=0, row=3)

        for b in self.winfo_children():
            b.grid(padx=1, pady=3, sticky="WE")


if __name__ == '__main__':
    pencere = App()
    pencere.mainloop()
