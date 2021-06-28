import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkinter.messagebox import *

FontBaslik = ("Verdana", 32)
FontAraBaslik = ("Arial", 16)
FontNormal = ("Arial", 12)


class App(tk.Tk):

    def __init__(self):  # constructor - kurucu
        super().__init__()
        self.title("Adres Defteri")
        self.geometry("1000x405-5+5")
        self.resizable(False, False)

        # Frame'leri düzgün dağıt
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.valIsim = tk.StringVar()
        self.valTel = tk.StringVar()
        self.valFoto = tk.StringVar()
        self.valNot = tk.StringVar()
        # içindekileri oluştur
        self.vtbaglan()
        self.alt_frameler()

    def alt_frameler(self):
        baslik = BaslikFrame(self, column=0, row=0)
        dugme_frame = ArabulFrame(self, column=2, row=0)
        verial_frame = VerialFrame(self, column=0, row=1)
        self.foto_frame = FotoFrame(self, column=3, row=0)
        self.menuFrame = MenuFrame(self, column=0, row=2)
        self.listFrame = ListFrame(self, column=1, row=2)
        self.listFrame.listele()

    def vtbaglan(self):
        self.baglan = sqlite3.connect("arasinav.db")
        self.cursor = self.baglan.cursor()
        sql = """create table if not exists `rehber` ( 
        id integer primary key autoincrement not null,
        isim text,
        numara text,
        foto text,
        nott text)
    """

        self.cursor.execute(sql)
        self.baglan.commit()


class BaslikFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        tk.Frame.__init__(self, sahip, bg="lightblue")
        self.config(relief=tk.RAISED, border=2)
        tk.Label(self, text="Adres Defteri", font=FontBaslik,
                 bg="lightblue").pack()
        self.grid(column=column, columnspan=2, row=row, padx=4, pady=4,
                  sticky="NEWS")


class ArabulFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.config(relief=tk.RAISED, border=2)
        self.relief = tk.GROOVE

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        isim = tk.Label(self, text="İsme Göre", font=FontNormal)
        isim.grid(column=0, row=0, sticky="NW")
        tel = tk.Label(self, text="Tele Göre", font=FontNormal)
        tel.grid(column=0, row=1, sticky="NW")

        araIsim = tk.Entry(self)
        araIsim.grid(column=1, row=0, sticky="NEWS")

        araTel = tk.Entry(self, bg="lightblue")
        araTel.grid(column=1, row=1, sticky="NEWS")

        self.grid(column=column, row=row, padx=4, pady=4, sticky="NEWS")


class FotoFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.sahip = sahip
        self.config(relief=tk.RAISED, border=2)
        self.bos_foto = tk.PhotoImage(file="./images/pengu1.png")

        self.foto = tk.Label(self, image=self.bos_foto)
        self.foto["image"] = self.bos_foto
        self.foto.pack(fill=tk.BOTH, expand=True)

        self.grid(column=column, row=row, rowspan=2, sticky="NEWS")

    def foto_degistir(self, foto):
        fotoyukle = tk.PhotoImage(file=foto)
        self.foto.photo = fotoyukle
        self.foto["image"] = fotoyukle


class MenuFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.sahip = sahip
        self.columnconfigure(0, weight=1)
        #        self.rowconfigure(0, weight=1)
        self.config(relief=tk.GROOVE, border=2)

        btn_kayit_ekle = tk.Button(self, text="Yeni Kayıt Ekle",
                                   command=self.kaydet)
        btn_kayit_ekle.grid(column=0, row=0, sticky="NEWS")
        btn_kayit_sil = tk.Button(self, text="Kayıt Sil", command=self.sil)
        btn_kayit_sil.grid(column=0, row=1, sticky="NEWS")
        btn_kayit_duzenle = tk.Button(self, text="Kayıt Düzenle",
                                      command=self.duzenle_kaydet)
        btn_kayit_duzenle.grid(column=0, row=2, sticky="NEWS")
        btn_kayit_sirala = tk.Button(self, text="İsme Göre Sırala",
                                     command=self.sirala)
        btn_kayit_sirala.grid(column=0, row=3, sticky="NEWS")
        btn_cik = tk.Button(self, text="Çıkış")
        btn_cik.grid(column=0, row=4, sticky="NEWS")

        self.grid(column=column, row=row, sticky="NEWS")

    def kaydet(self):
        sql = "insert into rehber (isim, numara, foto, nott) values ('{}'," \
              "'{}','{}','{}')".format(
            self.sahip.valIsim.get(),
            self.sahip.valTel.get(),
            self.sahip.valFoto.get(),
            self.sahip.valNot.get())

        self.sahip.valIsim.set("")
        self.sahip.valTel.set("")
        self.sahip.valFoto.set("")
        self.sahip.valNot.set("")

        self.sahip.cursor.execute(sql)
        self.sahip.baglan.commit()
        self.sahip.listFrame.listele()

    def sil(self):
        cevap = messagebox.askquestion('Sınav',
                                       'Seçili kayıtları silmek istediğinize emin misiniz?',
                                       icon="error")
        if cevap == "yes":
            for sil_id in self.sahip.tv.selection():
                sql = "delete from rehber where id={}".format(
                    self.sahip.tv.item(sil_id)['values'][0])
                self.sahip.cursor.execute(sql)
            self.sahip.baglan.commit()
            self.sahip.tv.delete(*self.sahip.tv.selection())

    def duzenle_aktar(self, object):
        a = self.sahip.tv.selection()[0]
        item = self.sahip.tv.item(a)
        print(item)
        self.sahip.ID = item['values'][0]
        self.sahip.valIsim.set(item['values'][1])
        self.sahip.valTel.set(item['values'][2])
        self.sahip.valFoto.set(item['values'][3])
        self.sahip.valNot.set(item['values'][4])

        self.sahip.baglan.commit()

    def duzenle_kaydet(self):
        if self.sahip.ID != 0:
            sql = "update rehber set isim='{}', numara='{}', foto='{}', " \
                  "nott='{}' where id={}".format(self.sahip.valIsim.get(),
                                                 self.sahip.valTel.get(),
                                                 self.sahip.valFoto.get(),
                                                 self.sahip.valNot.get(),
                                                 self.sahip.ID
                                                 )
            print(sql)
            self.sahip.cursor.execute(sql)
            self.sahip.baglan.commit()
            self.sahip.listFrame.listele()

    def sirala(self):
        self.sahip.listFrame.listele("isim")


class VerialFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        super().__init__(sahip)
        self.sahip = sahip
        self.config(relief=tk.GROOVE, border=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)

        isim = tk.Label(self, text="Adı Soyadı", font=FontNormal)
        isim.grid(column=0, row=0, sticky="NW")
        tel = tk.Label(self, text="Telefon Numarası", font=FontNormal)
        tel.grid(column=0, row=1, sticky="NW")
        foto = tk.Label(self, text="Fotoğraf", font=FontNormal)
        foto.grid(column=0, row=2, sticky="NW")
        nott = tk.Label(self, text="Not", font=FontNormal)
        nott.grid(column=0, row=3, sticky="NW")

        vIsim = tk.Entry(self, textvariable=sahip.valIsim)
        vIsim.grid(column=1, row=0, columnspan=2, sticky="NEW")

        vTel = tk.Entry(self, textvariable=sahip.valTel)
        vTel.grid(column=1, row=1, columnspan=2, sticky="NEW")

        vFoto = tk.Entry(self, textvariable=sahip.valFoto)
        vFoto.grid(column=1, row=2, sticky="NEW")

        vGozat = tk.Button(self, text="Gözat...", command=self.fotosec)
        vGozat.grid(column=2, row=2, sticky="NEWS")

        vNot = tk.Entry(self, textvariable=sahip.valNot)
        vNot.grid(column=1, row=3, columnspan=2, sticky="NEW")

        self.grid(column=column, row=row, columnspan=3, sticky="NEWS")

    def fotosec(self):
        dosya = filedialog.askopenfilename()
        print(dosya)
        self.sahip.valFoto.set(dosya)
        self.sahip.foto_frame.foto_degistir(dosya)


class ListFrame(tk.Frame):
    def __init__(self, sahip, column, row):
        tk.Frame.__init__(self, sahip)
        self.sahip = sahip
        self.columnconfigure(0, weight=1)
        self.config(relief=tk.GROOVE, border=2)

        self.tv = ttk.Treeview(self, show='headings')
        self.sahip.tv = self.tv
        ybar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=ybar.set)
        self.tv.grid(row=0, column=0, sticky="NEWS")
        self.tv['columns'] = ('id', 'isim', 'telefon', 'foto', 'not')

        self.tv.column('#0', width=0, stretch=tk.NO)
        self.tv.column('id', width=50, stretch=tk.NO)
        self.tv.column('isim', anchor=tk.CENTER)
        self.tv.column('telefon', anchor=tk.CENTER, width=80)
        self.tv.column('foto', anchor=tk.CENTER, width=80)
        self.tv.column('not', anchor=tk.CENTER, width=80)

        self.tv.heading('#0', text='', anchor=tk.CENTER)
        self.tv.heading('id', text='id', anchor=tk.CENTER)
        self.tv.heading('isim', text='Adı Soyadı', anchor=tk.CENTER)
        self.tv.heading('telefon', text='Telefon', anchor=tk.CENTER)
        self.tv.heading('foto', text='Foto', anchor=tk.CENTER)
        self.tv.heading('not', text='Not', anchor=tk.CENTER)

        self.tv.bind("<Double-1>", self.sahip.menuFrame.duzenle_aktar)
        self.grid(column=column, columnspan=3, row=row, sticky="NEWS")

    def listele(self, order="id"):
        self.tv.delete(*self.tv.get_children())
        sql = "select * from rehber order by " + order
        self.sahip.cursor.execute(sql)
        veriler = self.sahip.cursor.fetchall()

        for veri in veriler:
            self.tv.insert('', 'end', values=(
                veri[0], veri[1], veri[2], veri[3], veri[4]))


if __name__ == '__main__':
    pencere = App()
    pencere.mainloop()
