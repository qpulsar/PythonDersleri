import tkinter as tk

pencere = tk.Tk()
pencere.title("Başlık")
pencere.geometry("200x200-100+50")
pencere.resizable(width=False, height=False)

#metin kutusu oluştur
metin = tk.Label(text="Merhaba GUI dünyası",
                 fg="red", bg="lightblue")

metin.pack()
print("deneme")
pencere.mainloop()
