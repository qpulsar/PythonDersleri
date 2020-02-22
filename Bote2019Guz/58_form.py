from tkinter import *
from tkinter import messagebox

import sqlite3

register_view = False
sgn_window = None
baglanti = None
db = None
rusername = None
ruserpass = None

def connectDB():
    global baglanti
    global db
    try:
        baglanti = sqlite3.connect("veritabani.db")
    except:
        print("Veri Tabanı bağlantısında hata!")
        exit()

    db = baglanti.cursor()
    db.execute("""
    create table if not exists kullanicilar(
    id integer primary key autoincrement,
    isim text,
    parola text)
    """)
    baglanti.commit()



def newUser():
    global rusername
    global ruserpass
    connectDB()

    sql = "select * from kullanicilar where isim like '{}'".format(rusername.get())
    print (sql)
    sonuc = db.execute(sql)
    kayitlar = sonuc.fetchall()
    if len(kayitlar)>0:
        messagebox.showinfo("Hata", "Kullanıcı adı daha önceden alınmış.")
        ruserpass.set("")
        rusername.set("")
        return
    sql = "insert into kullanicilar (isim, parola) values ('{}','{}')".format(rusername.get(),
                                                                           ruserpass.get())
    db.execute(sql)
    baglanti.commit()


def clear():
    username.set("")
    userpass.set("")


def signup_onclose():
    global register_view
    global sgn_window
    register_view = False
    sgn_window.destroy()


def signup():
    global register_view
    global sgn_window
    global rusername
    global ruserpass

    if register_view == False:
        register_view = True
        sgn_window = Toplevel(root)
        sgn_window.geometry("-100+100")
        sgn_window.title("Kayıt Ol")
        sgn_window.protocol("WM_DELETE_WINDOW", signup_onclose)
        lbl_signup = Label(sgn_window, text="KAYIT OL", bg="DarkSlateGray1")
        lbl_signup.grid(row=0, column=0, columnspan=2)
        lbl_user = Label(sgn_window, text="Kullanıcı Adı", anchor=E, bg="skyblue1", padx=10)
        lbl_user.grid(row=1, column=0, sticky="EW")
        lbl_pass = Label(sgn_window, text="Parola", anchor=E, bg="skyblue1", padx=10)
        lbl_pass.grid(row=2, column=0, sticky="EW")
        rusername = StringVar()
        ruserpass = StringVar()

        e_user = Entry(sgn_window, textvariable=rusername)
        e_user.grid(row=1, column=1)
        e_pass = Entry(sgn_window, textvariable=ruserpass, show='*')
        e_pass.grid(row=2, column=1)
        btn_login = Button(sgn_window, text="Kaydol", command=newUser)
        btn_login.grid(row=3, column=0, columnspan=2)


root = Tk()
root.title("Login")
root.geometry("-50+100")

lbl_baslik = Label(root, text="LOGIN", justify=CENTER, bg="tomato")
lbl_baslik.grid(row=0, column=0, columnspan=3, sticky="NEWS")

lbl_user = Label(root, text="Kullanıcı Adı", anchor=E, bg="skyblue1", padx=10)
lbl_user.grid(row=1, column=0, sticky="EW")
lbl_pass = Label(root, text="Parola", anchor=E, bg="skyblue1", padx=10)
lbl_pass.grid(row=2, column=0, sticky="EW")

username = StringVar()
userpass = StringVar()

e_user = Entry(root, textvariable=username)
e_user.grid(row=1, column=1)
e_pass = Entry(root, textvariable=userpass, show='*')
e_pass.grid(row=2, column=1)

frm_buttons = Frame(root)
frm_buttons.grid(row=3, column=0, columnspan=3)
btn_clear = Button(frm_buttons, text="Temizle", command=clear)
btn_clear.grid(row=0, column=0)
btn_login = Button(frm_buttons, text="Giriş", command=clear)
btn_login.grid(row=0, column=1)

frm_signup = Frame(root)
frm_signup.grid(row=4, column=0, columnspan=3)
btn_signup = Button(frm_signup, text="Kayıtol", command=signup)
btn_signup.grid(row=0, column=0)

userimage = PhotoImage(file="./images/user.png")
lbl_avatar = Label(root, image=userimage)
lbl_avatar.grid(row=1, column=2, rowspan=2)

root.mainloop()
