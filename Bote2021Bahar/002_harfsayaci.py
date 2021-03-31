class HarfSay:
    sesli_harfler = "aeıioöuü"

    def __init__(self):
        self.sayac = 0

    def kelime_al(self):
        return input("Bir kelime giriniz:")

    def seslimi(self, harf):
        return harf in HarfSay.sesli_harfler

    def saydir(self):
        for harf in self.kelime:
            if self.seslimi(harf):
                self.sayac += 1

    def ekrana_yaz(self):
        print(
            "{} kelimesinde {} harf seslidir.".format(self.kelime, self.sayac))

    def calistir(self):
        self.kelime = self.kelime_al()
        self.saydir()
        self.ekrana_yaz()


bune = HarfSay()
bune.calistir()

bidaha = HarfSay()
bidaha.calistir()
