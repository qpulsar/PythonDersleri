"""
Verilen iki sayının toplamını bulan fonksiyonu yazınız
"""


def gizemli(s1, s2):
    son = s1 + s2
    print(son)


def topla(sayi1, sayi2):
    return sayi1 + sayi2


def isteneni_topla():
    s1 = int(input("Birinci sayı:"))
    s2 = int(input("Birinci sayı:"))
    print(s1 + s2)


isteneni_topla()
print(topla(5, 8))
sonuc = topla(5, 5)
print(sonuc)

print(gizemli(9, 7))
