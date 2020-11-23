"""
Verilen listenin elemanlarının toplamını döngü kullanarak bulan fonksiyonu yapınız
"""


def list_topla(d):
    toplam = 0
    for i in d:
        toplam += i
    return toplam


def kadar_toplam(sinir):
    toplam = 0
    for i in range(1, sinir + 1):
        toplam += i
    return toplam


dizi = [5, 2, 7, 1, 7, 2, 7, 5, 3, 1, 67, 9]
print(list_topla(dizi))


print(kadar_toplam(10))
