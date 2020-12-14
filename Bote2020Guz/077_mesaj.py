from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Mesaj kutusu")
window.geometry("300x300-10+10")


def mesaj_ver():
    messagebox.showinfo("Başlık", "İçerik")
    messagebox.showwarning("Dikkat", "Uyarı yapıyorum")
    messagebox.showerror("Hata", "Yanlış yaptın")


def yanit():
    cvp = messagebox.askyesno("Evet Hayır", "Mezun olmak ister misin?")
    print(cvp)


btn = Button(window, text="Mesaj al", command=mesaj_ver)
btn.pack()

btn1 = Button(window, text="etkileşim", command=yanit)
btn1.pack()

window.mainloop()
