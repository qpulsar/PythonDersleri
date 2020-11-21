"""
0 yazıncaya kadar girilen sayıların toplamını bulan program
"""

print("Çıkmak için 0 giriniz")

sayi = None
toplam = 0
while sayi != 0:
    sayi = int(input("sayı:"))
    toplam = toplam + sayi

print("toplam = ", toplam)
