import random

dizi = []
for i in range(0, 10):
    sayi = random.randrange(1, 10)
    while sayi in dizi:
        print("aynısı var", sayi)
        sayi = random.randrange(1, 11)
    dizi.append(sayi)

print(dizi)
