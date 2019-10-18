sayilar = []

sayi = None

while sayi != 0:
    sayi = int(input("Bir sayı giriniz:"))
    sayilar.append(sayi)

sayilar.pop()
sayilar.sort()
print("Girdiğini sayılar:", sayilar)