from tkinter import *
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("BASIT CRUD")
root.geometry("1000x500-0+100")


def vtbaglan():
    global baglan, cursor
    baglan = sqlite3.connect("obs.db")
    cursor = baglan.cursor()
    sql = """create table if not exists `ogrenci` ( 
    id integer primary key autoincrement not null,
    isim text,
    numara text,
    vize integer,
    fin integer,
    but integer)
"""
    cursor.execute(sql)
    lbl_sonuc["text"] = "VT Bağlantısı yapıldı."
    lbl_sonuc["bg"] = "lightgreen"
    baglan.commit()


def yeni_kayit():
    if isim.get() == "" or numara.get() == "" or vize.get() < 0 or fin.get() < 0 or but.get() < 0 \
            or vize.get() > 100 or fin.get() > 100 or but.get() > 100:
        lbl_sonuc["text"] = "Eksik veri girişi."
        lbl_sonuc["bg"] = "tomato"
    else:
        lbl_sonuc["text"] = "Veriler kaydedildi."
        lbl_sonuc["bg"] = "lightblue"
        sql = "insert into ogrenci (isim,numara, vize, fin, but) values ('{}','{}',{},{},{})".format(isim.get(),
                                numara.get(), vize.get(), fin.get(), but.get())

        cursor.execute(sql)
        baglan.commit()

def oku():
    pass

isim = StringVar()
numara = StringVar()
vize = IntVar()
fin = IntVar()
but = IntVar()

ust = Frame(root, width=1000, height=50, relief=GROOVE, bd=5)
ust.pack(side=TOP)
sol = Frame(root, width=400, height=450, relief=RAISED, bd=3)
sol.pack(side=LEFT, expand=True, fill=BOTH)
sag = Frame(root, width=600, height=450, relief=RAISED, bd=3)
sag.pack(side=RIGHT, expand=True, fill=BOTH)

formFrame = Frame(sol, width=400, height=350, relief=GROOVE, bd=3)
formFrame.pack(side=TOP, expand=True, fill=BOTH)
dugmeFrame = Frame(sol, width=400, height=100, relief=GROOVE, bd=3)
dugmeFrame.pack(side=BOTTOM)

lbl_baslik = Label(ust, width=900, font=('Arial', 30), text="CRUD Uygulaması")
lbl_baslik.pack()
fo = ("Times New Roman", 16)
lbl_isim = Label(formFrame, text="İsim", font=fo, relief=FLAT)
lbl_isim.grid(row=0, column=0, sticky=E)
lbl_numara = Label(formFrame, text="Numara", font=fo, relief=FLAT)
lbl_numara.grid(row=1, column=0, sticky=E)
lbl_vize = Label(formFrame, text="Vize Notu", font=fo, relief=FLAT)
lbl_vize.grid(row=2, column=0, sticky=E)
lbl_final = Label(formFrame, text="Final Notu", font=fo, relief=FLAT)
lbl_final.grid(row=3, column=0, sticky=E)
lbl_but = Label(formFrame, text="Bütünleme notu", font=fo, relief=FLAT)
lbl_but.grid(row=4, column=0, sticky=E)

lbl_sonuc = Label(formFrame, text="...", font=fo, relief=SUNKEN)
lbl_sonuc.grid(row=5, column=0, columnspan=2, sticky=EW)

e_isim = Entry(formFrame, textvariable=isim, font=fo, width=30)
e_isim.grid(row=0, column=1, sticky=W)
e_numara = Entry(formFrame, textvariable=numara, font=fo, width=15)
e_numara.grid(row=1, column=1, sticky=W)
e_vize = Entry(formFrame, textvariable=vize, font=fo, width=15)
e_vize.grid(row=2, column=1, sticky=W)
e_fin = Entry(formFrame, textvariable=fin, font=fo, width=15)
e_fin.grid(row=3, column=1, sticky=W)
e_but = Entry(formFrame, textvariable=but, font=fo, width=15)
e_but.grid(row=4, column=1, sticky=W)

btn_yeni = Button(dugmeFrame, width=10, text="kaydet", command=yeni_kayit)
btn_yeni.pack(side=LEFT)
btn_oku = Button(dugmeFrame, width=10, text="Oku")
btn_oku.pack(side=LEFT)
btn_guncelle = Button(dugmeFrame, width=10, text="Güncelle")
btn_guncelle.pack(side=LEFT)
btn_sil = Button(dugmeFrame, width=10, text="Sil")
btn_sil.pack(side=LEFT)
btn_cik = Button(dugmeFrame, width=10, text="Çıkış")
btn_cik.pack(side=LEFT)

skrol_yatay = Scrollbar(sag, orient=HORIZONTAL)
skrol_dikey = Scrollbar(sag, orient=VERTICAL)

tree = ttk.Treeview(sag,
                    columns=("SN", "İsim", "Numara", "Vize", "Final", "Bütünleme", "Ortalama", "Sonuç"),
                    selectmode="extended", height=450, yscrollcommand=skrol_dikey.set, xscrollcommand=skrol_yatay.set)
skrol_dikey["command"] = tree.yview
skrol_dikey.pack(side=RIGHT, fill=Y)
skrol_yatay["command"] = tree.xview
skrol_yatay.pack(side=BOTTOM, fill=X)
tree.heading('SN', text="SN", anchor=W)
tree.heading('İsim', text="İsim", anchor=W)
tree.heading('Numara', text="Numara", anchor=W)
tree.heading('Vize', text="Vize", anchor=W)
tree.heading('Final', text="Final", anchor=W)
tree.heading('Bütünleme', text="Bütünleme", anchor=W)
tree.heading('Ortalama', text="Ortalama", anchor=W)
tree.heading('Sonuç', text="Sonuç", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=30)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=100)
tree.column('#4', stretch=NO, minwidth=0, width=50)
tree.column('#5', stretch=NO, minwidth=0, width=50)
tree.column('#6', stretch=NO, minwidth=0, width=50)
tree.column('#7', stretch=NO, minwidth=0, width=50)
tree.column('#8', stretch=NO, minwidth=0, width=50)

tree.pack()

vtbaglan()
root.mainloop()
