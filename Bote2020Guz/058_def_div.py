"""
Parametre olarak liste içinde verilen sayıların yine parametre
 olarak verilen sayıya tam bölünenleri liste olarak geri döndüren fonksiyonu yazınız
"""


def bol_bul(dizi, bolen):
    sonuc = []
    for i in dizi:
        if i % bolen == 0:
            sonuc.append(i)
    return sonuc


sayilar = [1, 4, 67, 8, 32, 2, 4, 6]
print(bol_bul(sayilar, 2))


sayilar = [1, 4, 67, 8, 32, 2, 4, 6]
print(bol_bul(sayilar,  2))
