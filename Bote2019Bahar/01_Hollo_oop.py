#sınıf
class Kus:
    tur = "kus"

    def bilgi(self):
        print(self.tur)

    #constructor
    def __init__(self, t):
        print("Merhaba ben yeni bir nesneyim")
        self.tur = t

    def yetenek(self):
        print("Uçarım")


class DeveKusu(Kus):
    def __init__(self):
        super(DeveKusu, self).__init__("devekuşu")

    def yetenek(self):
        print("Kaçarım")

d = DeveKusu()
d.bilgi()
d.yetenek()

#nesne
serce = Kus("serçe")
serce.bilgi()
serce.yetenek()
serce.bilgi()

karga = Kus("Siyah Kuş")
karga.bilgi()

