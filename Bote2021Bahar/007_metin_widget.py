import tkinter as tk


class MetinWidget(tk.Frame):
    def __init__(self, sahip):
        super().__init__(sahip)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.olustur()
        self.pack()

    def olustur(self):
        self.label = tk.Label(self, text="isim")
        self.label.grid(column=0, row=0, sticky=tk.W)
        self.giris = tk.Entry(self, width=20)
        self.giris.focus()
        self.giris.grid(column=1, row=0, sticky=tk.W)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Widget Üretim Merkezi")
        self.geometry("400x500")
        MetinWidget(self)
        MetinWidget(self)
        MetinWidget(self)
        MetinWidget(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()
