import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class Donsturucu:
    @staticmethod
    def fah_tan_cel(f, format=True):
        sonuc = (f - 32) * 5 / 9
        if format:
            return f"{f} Fahrenheit = {sonuc:.2f} Celcius derece."
        else:
            sonuc

    @staticmethod
    def cel_tan_fah(c, format=True):
        sonuc = c * 9 / 5 + 32
        if format:
            return f"{c} Celcius = {sonuc:.2f} Fahrenheit derece."
        else:
            sonuc


class KontrolFrame(ttk.LabelFrame):
    def __init__(self, sahip):
        super().__init__(sahip)
        self.relief = "GROOVE"
        self["text"] = "Seçiminiz"
        self.secilen_radio = tk.IntVar()

        ttk.Radiobutton(self, text="C->F", value=0,
                        variable=self.secilen_radio,
                        command=self.frame_degistir).grid(column=0, row=0,
                                                          padx=4, pady=4,
                                                          )
        ttk.Radiobutton(self, text="F->C", value=1,
                        variable=self.secilen_radio,
                        command=self.frame_degistir).grid(column=1, row=0,
                                                          padx=4, pady=4,
                                                          )

        # Değiştirelecek olan frame'ler
        self.frameler = {}
        self.frameler[0] = DonusenFrame(sahip, 'Celcius',
                                        Donsturucu.cel_tan_fah)
        self.frameler[1] = DonusenFrame(sahip, 'Fahrenheit',
                                        Donsturucu.fah_tan_cel)

        self.frame_degistir()

        self.grid(column=0, row=1, padx=4, pady=4, sticky="EW")

    def frame_degistir(self):
        frame = self.frameler[self.secilen_radio.get()]
        #frame.reset()
        frame.tkraise()


class DonusenFrame(ttk.Frame):
    def __init__(self, sahip, hangisi, fonk):
        super().__init__(sahip)

        self.hangisi = hangisi
        self.fonk = fonk

        self.label = ttk.Label(self, text=hangisi)
        self.label.grid(column=0, row=0)

        self.temp = tk.StringVar()
        self.temp_entry = ttk.Entry(self, textvariable=self.temp)
        self.temp_entry.grid(column=1, row=0)
        self.temp_entry.focus()

        self.donustur = ttk.Button(self, text="Dönüştür", command=self.fonk)
        self.donustur.grid(column=2, row=0)

        self.grid(row=0, column=0, sticky="news")



class Program(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sıcaklık dönüştürücü")
        self.geometry("300x140")
        self.resizable(0, 0)


if __name__ == '__main__':
    program = Program()
    KontrolFrame(program)
    program.mainloop()
