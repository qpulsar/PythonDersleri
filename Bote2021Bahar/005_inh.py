import tkinter as tk


class Uygulama(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Burası başlık")
        self.geometry("300x300")

        self.label = tk.Label(self, text="Ben tkinterım artık")
        self.label.pack()

        self.buton = tk.Button(self, text="Bana tıkla", command=self.tik)
        self.buton.pack()

    def tik(self):
        self.label["text"] = "Butonu tıkladılar..."


u = Uygulama()
u.mainloop()
