"""
Verilen sayının faktöriyelini hesaplayan fonksiyonu yazınız
5! = 5*4*3*2*1 = 125
"""


def faktor(s):
    f = 1
    for i in range(2, s + 1):
        f *= i
    return f


sonuc = faktor(5)
print(sonuc)

