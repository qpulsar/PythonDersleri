print("Çıkmak için 0 giriniz.")

sayi = None
toplam = 0
while sayi != 0:
    sayi = int(input("Sayı:"))
    toplam += sayi  # toplam = toplam + sayi

print("Girilen sayıların toplamı = ", toplam)
