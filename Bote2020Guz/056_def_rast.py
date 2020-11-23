"""
İstenen aralık ve sayıda sayıyı rastgele üreten ve sonucu liste olarak döndüren fonksiyonu yazınız
"""
import random


def rast_dizi(ilk, son, adet):
    dizi = []
    for i in range(1, adet + 1):
        dizi.append(random.randrange(ilk, son + 1))

    return dizi


print(rast_dizi(20, 40, 10))
