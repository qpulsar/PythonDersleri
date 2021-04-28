import tkinter as tk


class Gui:
    ek = 1
    def __init__(self, root):
        self.root = root
        buton = tk.Button(root, text="Label ekle", command=self.ekle)
        buton.pack()

    def ekle(self):

        a = tk.Label(text=f"Eklenen:{self.ek}", font=("Arial, 20"))
        a.pack()
        self.ek += 1


pencere = tk.Tk()
g = Gui(pencere)
pencere.mainloop()
