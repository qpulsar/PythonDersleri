# KULLANILACAK MODÜLLERİ TANITMA
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
from tkinter import *

# VERİ TABANI OLUŞTURMA

vt = sqlite3.connect('depo.db')
im = vt.cursor()
im.execute("create table if not exists urun(urun_adi TEXT, urun_fiyati TEXT, urun_kdv TEXT)")
im.execute("create table if not exists stok(urun_id integer,urun_adi TEXT, adet integer)")
vt.commit()


# MESAJLAR

def mesaj1(text):
    msg = messagebox.showinfo(text, "Kayıt Başarılı !")


def mesaj2(text):
    msg = messagebox.showerror(text, "Bu isimde Ürün Kayıtlı!")


def mesaj3(text):
    msg = messagebox.showinfo(text, "Kayıt Silindi!")

def mesaj4(text):
    msg = messagebox.showinfo(text, "Kaydınız Güncellendi!")


# MENÜ PENCERESİ
def ana_menu():
    for i in pencere.winfo_children():
        i.destroy()
    pencere.title("MENÜ")
    urun_buton = Button(text="ÜRÜN EKRANI", command=urun_pencere).place(x=60, y=155, width=150, height=40)
    stok_buton = Button(text="STOK EKRANI", command=stok_menu).place(x=290, y=155, width=150, height=40)

# STOK MENÜSÜ PENCERESİ

def stok_menu():


    for i in pencere.winfo_children():
        i.destroy()
    pencere.title("STOK")
    stok_ekle = Button(text="ÜRÜN EKLE").place(x=20, y=20, width=180, height=30)
    stok_cikart = Button(text="ÜRÜN ÇIKART").place(x=20, y=60, width=180, height=30)
    stok_menu = Button(text="ANA MENÜ", command=ana_menu).place(x=20, y=100, width=180, height=30)

    Label(text="Ürün Adı", font="Verdana 10 ").place(x=230, y=40)
    Label(text="Ürün Adedi", font="Verdana 10 ").place(x=230, y=80)

    combo= Combobox()
    combo['values']=("ercu","ahmet","mehmet")
    combo.place(x=320,y=60)

    gir4 = Entry(width=26)
    gir4.place(x=320, y=80)

    liste = Treeview(pencere)
    liste["columns"] = ("id_no", "Ad", "adet")
    liste.column('#0', width=0, stretch=NO)
    liste.column('id_no', width=20, anchor=CENTER)
    liste.column('Ad', anchor=CENTER, width=220)
    liste.column('adet', anchor=CENTER, width=100)

    liste.place(x=20, y=140, width=460, height=180)
    liste.heading("#0", text="")
    liste.heading("id_no", text="ID")
    liste.heading("Ad", text="Ürün Adı")
    liste.heading("adet", text="Adet")

    im.execute("""SELECT urun_id,urun_adi, adet FROM stok""")
    stok_liste = im.fetchall()
    for i in stok_liste:
        liste.insert(parent='', index='end', values=(i[0],i[1],i[2]))


# ÜRÜN MENÜSÜ PENCERESİ

def urun_pencere():
    # ÜRÜN KATIT BÖLÜMÜ
    def urun_ekle():
        a = gir1.get()
        b = gir2.get()
        c = gir3.get()

        def degerle():
            im.execute("insert into urun values(?,?,?)", [a, b, c])
            vt.commit()

            #STOK VERI TABANINA YAZMA
            im.execute("""SELECT rowid,urun_adi FROM urun""")
            kontrol_ara = im.fetchall()
            for i in kontrol_ara:
                stok_ad_kontrol = i[1]
                ur_id_no=i[0]
                if stok_ad_kontrol == a:
                    im.execute("insert into stok values(?,?,?)", [ur_id_no,a, '0'])
                    vt.commit()

        kod = 0
        im.execute("""SELECT urun_adi FROM urun""")
        kontrol = im.fetchall()
        for i in kontrol:
            ad_kontrol = i[0]
            if ad_kontrol == a:
                mesaj2("KAYIT VAR")
                kod = 1
        if kod == 0:
            degerle()
            mesaj1("KAYIT")
            gir1.delete(0, "end")
            gir2.delete(0, "end")
            gir3.delete(0, "end")

            for i in liste.get_children():
                liste.delete(i)
            im.execute("""SELECT rowid,urun_adi,urun_fiyati, urun_kdv  FROM urun""")
            urun_liste = im.fetchall()
            for i in urun_liste:
                liste.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3]))

    def urun_silme():
        s = gir1.get()
        # STOKTAN KAYIT SILME
        im.execute("""SELECT rowid,urun_adi FROM urun""")
        kontrol_ara = im.fetchall()
        for i in kontrol_ara:
            stok_ad_kontrol = i[1]
            if stok_ad_kontrol == s:
                sil_id=i[0]
        msg = messagebox.askyesno("SİLME İŞLEMİ", "EMİN MİSİN?")
        if msg == True:
            im.execute("delete from urun where urun_adi= ? ", [s])
            im.execute("delete from stok where urun_id= ? ", [sil_id])
            vt.commit()
            gir1.delete(0, "end")
            gir2.delete(0, "end")
            gir3.delete(0, "end")
            mesaj3("SİLME")
            for i in liste.get_children():
                liste.delete(i)
            im.execute("""SELECT rowid,urun_adi,urun_fiyati, urun_kdv  FROM urun""")
            urun_liste = im.fetchall()
            for i in urun_liste:
                liste.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3]))

#KAYIT GÜNCELLEME
    def urun_guncelle():
        al = liste.selection()[0]
        item = liste.item(al)
        sec_id_no = item['values'][0]

        im.execute("update urun set urun_adi='{}',urun_fiyati='{}',urun_kdv='{}' WHERE rowid='{}'".format(gir1.get(),
                                                                                                          gir2.get(),
                                                                                                          gir3.get(),
                                                                                                          sec_id_no))
        vt.commit()

        gir1.delete(0, "end")
        gir2.delete(0, "end")
        gir3.delete(0, "end")
        mesaj4("GÜNCELLEME")
        for i in liste.get_children():
            liste.delete(i)
        im.execute("""SELECT rowid,urun_adi,urun_fiyati, urun_kdv  FROM urun""")
        urun_liste = im.fetchall()
        for i in urun_liste:
            liste.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3]))



    for i in pencere.winfo_children():
        i.destroy()

    pencere.title("ÜRÜN")
    Label(text="Ürün Adı", font="Verdana 10 ").place(x=10, y=30)
    Label(text="Ürün Fiyatı", font="Verdana 10 ").place(x=10, y=60)
    Label(text="KDV", font="Verdana 10 ").place(x=10, y=90)

    gir1 = Entry(width=30)
    gir1.place(x=100, y=30)
    gir2 = Entry(width=30)
    gir2.place(x=100, y=60)
    gir3 = Entry(width=30)
    gir3.place(x=100, y=90)

    urun_kaydet = Button(text="KAYDET", command=urun_ekle).place(x=300, y=30, width=80, height=30)
    urun_guncelle = Button(text="GÜNCELLE", command=urun_guncelle).place(x=400, y=30, width=80, height=30)
    urun_sil = Button(text="SİL", command=urun_silme).place(x=300, y=80, width=80, height=30)
    urun_menu = Button(text="ANA MENÜ", command=ana_menu).place(x=400, y=80, width=80, height=30)

    liste = Treeview(pencere)
    liste["columns"] = ("id_no", "Ad", "fiyat", "kdv")
    liste.column('#0', width=0, stretch=NO)
    liste.column('id_no', width=20, anchor=CENTER)
    liste.column('Ad', anchor=CENTER, width=220)
    liste.column('fiyat', anchor=CENTER, width=100)
    liste.column('kdv', anchor=CENTER, width=100)

    liste.place(x=20, y=140, width=460, height=180)
    liste.heading("#0", text="")
    liste.heading("id_no", text="ID")
    liste.heading("Ad", text="Ürün Adı")
    liste.heading("fiyat", text="Ürün Fiyatı")
    liste.heading("kdv", text="KDV %")

    im.execute("""SELECT rowid,urun_adi,urun_fiyati, urun_kdv  FROM urun""")
    urun_liste = im.fetchall()
    for i in urun_liste:
        liste.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3]))

    def aktarma(object):
        gir1.delete(0, "end")
        gir2.delete(0, "end")
        gir3.delete(0, "end")
        al = liste.selection()[0]
        item = liste.item(al)
        gir1.insert(0, item['values'][1])
        gir2.insert(0, item['values'][2])
        gir3.insert(0, item['values'][3])

    liste.bind("<Double-1>", aktarma)


# PENCERE OLUŞTURMA
pencere = tk.Tk()
pencere.geometry("500x350+500+200")
pencere.resizable(False, False)
ana_menu()

pencere.mainloop()
