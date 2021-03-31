class Kopek():
    tur = "Golden"
    sayac = 0

    # constructor - nesne oluşturuluken otomatik olarak çağrılıır
    def __init__(self, ad):
        self.kopek_ad = ad
        print("Hav hav", ad)
        Kopek.sayac += 1

    def yakala(self):
        print("Topu getirdim", self.kopek_ad)


boncuk = Kopek("Boncuk")
boncuk.yakala()

lessi = Kopek("Lessi")
a = Kopek("a")
b = Kopek("b")
c = Kopek("c")
print(lessi.tur)
print(boncuk.tur)
print("Köpek sayısı:", lessi.sayac)
