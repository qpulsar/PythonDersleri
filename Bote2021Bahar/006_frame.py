import tkinter as tk
from tkinter.messagebox import showinfo

class MainFrame(tk.Frame):
    def __init__(self, sahip):
        super().__init__(sahip)

        self.label = tk.Label(self, text="Frame için label")
        self.label.pack()

        self.button = tk.Button(self, text="Bana tıkla")
        self.button["command"] = self.tiklandi
        self.button.pack()

        self.pack() #kendini pencereye ekle

    def tiklandi(self):
        showinfo(title="Bilgilendirme", message="Bu konular sınava "
                                                   "dahildir.")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bu pencere")
        self.geometry("300x300")


if __name__ == '__main__':
    app = App()
    frame = MainFrame(app)
    app.mainloop()
