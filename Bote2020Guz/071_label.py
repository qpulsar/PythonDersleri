import tkinter as tk

pencere = tk.Tk()
pencere.title("BÖTE")
pencere.geometry("300x200+1000+100")
pencere.resizable(width=False, height=True)

# Yazı (etiket)

metin = tk.Label(text="Merhaba BÖTE")
metin.pack()

pencere.mainloop()
