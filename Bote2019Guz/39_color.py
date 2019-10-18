import tkinter as tk

pencere = tk.Tk()
pencere.title("Başlık")
pencere.geometry("200x200+100-50")

#metin kutusu oluştur
metin = tk.Label(text="İnşallah haftaya import ederiz",
                 fg="red", bg="lightblue")

metin.pack()
print("deneme")
pencere.mainloop()