import tkinter as tk
import sqlite3
from tkinter import ttk

FontBaslik = ("Verdana", 32)
FontNormal = ("Arial", 12)


class App(tk.Tk):
    def __init__(self):  # constructor
        super().__init__()
        self.title("Adres Defteri")
        self.geometry("1000x426-5+10")
        self.resizable(False, False)

        self.frame_olustur()

    def frame_olustur(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        baslikFrame = BaslikFrame(self, column=0, row=0)
        arabulFrame = ArabulFrame(self, column=2, row=0)
        fotoFrame = FotoFrame(self, column=3, row=0)
        menuFrame = MenuFrame(self, column=0, row=2)
        veriGiris = VeriGirisFrame(self, column=0, row=1)
        listFrame = ListFrame(self, column=1, row=2)


class ListFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.columnconfigure(0, weight=1)
        self.configure(relief=tk.GROOVE, border=2)
        self.tv = ttk.Treeview(self, show="headings")
        ybar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=ybar.set)
        self.tv.grid(column=0, row=0, sticky="NEWS")
        self.tv['column'] = ('id', 'isim', 'telefon', 'foto', 'not')

        self.tv.column('#0', width=0, stretch=tk.NO)
        self.tv.column('id', width=80, anchor=tk.E)
        self.tv.column('isim', anchor=tk.CENTER)
        self.tv.column('telefon', width=100, anchor=tk.W)
        self.tv.column('foto', width=100, anchor=tk.W)
        self.tv.column('not', width=100, anchor=tk.W)

        self.tv.heading('#0', text='', anchor=tk.CENTER)
        self.tv.heading('id', text='ID', anchor=tk.CENTER)
        self.tv.heading('isim', text='Adı Soyadı', anchor=tk.CENTER)
        self.tv.heading('telefon', text='Telefon', anchor=tk.CENTER)
        self.tv.heading('foto', text='Fotoğraf', anchor=tk.CENTER)
        self.tv.heading('not', text='Açıklama', anchor=tk.CENTER)

        self.grid(column=column, row=row, columnspan=4, sticky="NEWS", padx=5,
                  pady=5)


class VeriGirisFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.configure(relief=tk.GROOVE, border=2)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)

        isim = tk.Label(self, text="Adı Soyadı", font=FontNormal)
        isim.grid(column=0, row=0, sticky="NW")
        telefon = tk.Label(self, text="Telefon Numarası", font=FontNormal)
        telefon.grid(column=0, row=1, sticky="NW")
        foto = tk.Label(self, text="Fotoğraf", font=FontNormal)
        foto.grid(column=0, row=2, sticky="NW")
        nott = tk.Label(self, text="Açıklama", font=FontNormal)
        nott.grid(column=0, row=3, sticky="NW")

        eIsim = tk.Entry(self)
        eIsim.grid(column=1, row=0, columnspan=2, sticky="NWES")
        eTel = tk.Entry(self)
        eTel.grid(column=1, row=1, columnspan=2, sticky="NWES")
        eFoto = tk.Entry(self)
        eFoto.grid(column=1, row=2, sticky="NWES")
        eNot = tk.Entry(self)
        eNot.grid(column=1, row=3, columnspan=2, sticky="NWES")

        gozat = tk.Button(self, text="Gözat")
        gozat.grid(row=2, column=2, sticky="NWES")

        self.grid(column=column, row=row, sticky="NEWS", columnspan=3, padx=5,
                  pady=5)


class BaslikFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        tk.Frame.__init__(self, sahip, bg="lightblue")
        self.configure(relief=tk.RAISED, border=2)
        tk.Label(self, text="Adres Defteri", font=FontBaslik,
                 bg="lightblue").pack()
        self.grid(column=column, row=row, columnspan=2, sticky="NEWS", padx=5,
                  pady=5)


class ArabulFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.configure(relief=tk.GROOVE, border=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        isim = tk.Label(self, text="İsme Göre", font=FontNormal)
        isim.grid(column=0, row=0)
        tel = tk.Label(self, text="Telefona Göre", font=FontNormal)
        tel.grid(column=0, row=1)

        araIsim = tk.Entry(self, bg="bisque1")
        araIsim.grid(column=1, row=0, sticky="NEWS")

        araTel = tk.Entry(self, bg="bisque2")
        araTel.grid(column=1, row=1, sticky="NEWS")

        self.grid(column=column, row=row, sticky="NEWS", padx=5, pady=5)


class FotoFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.configure(relief=tk.GROOVE)

        self.bos_foto = tk.PhotoImage(file="./images/pengu1.png")

        self.foto = tk.Label(self, image=self.bos_foto)
        # self.foto.photo = self.bos_foto
        self.foto["image"] = self.bos_foto
        self.foto.pack(fill=tk.BOTH, expand=True)

        self.grid(column=column, row=row, rowspan=2, sticky="NEWS", padx=5,
                  pady=5)


class MenuFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.configure(relief=tk.GROOVE, border=2)
        self.columnconfigure(0, weight=1)

        for i in range(0, 5):
            self.rowconfigure(i, weight=1)

        btn_kayit_ekle = tk.Button(self, text="Yeni Kayıt Ekle")
        btn_kayit_ekle.grid(column=0, row=0, sticky="NEWS")

        btn_kayit_sil = tk.Button(self, text="Kayıt Sil")
        btn_kayit_sil.grid(column=0, row=1, sticky="NEWS")

        btn_kayit_duzenle = tk.Button(self, text="Kayıt Düzenle")
        btn_kayit_duzenle.grid(column=0, row=2, sticky="NEWS")

        btn_sirala = tk.Button(self, text="İsme Göre Sırala")
        btn_sirala.grid(column=0, row=3, sticky="NEWS")

        btn_cik = tk.Button(self, text="Programdan Çık", bg="lightcoral")
        btn_cik.grid(column=0, row=4, sticky="NEWS")

        self.grid(column=column, row=row, sticky="NEWS", padx=5, pady=5)


if __name__ == '__main__':
    pencere = App()
    pencere.mainloop()
