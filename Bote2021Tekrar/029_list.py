import random
#boş
dizi = [5, 8, 4, 32, 6, 3, 2, 6, 8, 32, 1, 53, 1, 77]

print(dizi)
print(dizi[5:])
print(dizi[3:6])
print(dizi[3:10:2])
print(dizi[3:3 + 8:1])
print(dizi[3::3])
print(dizi[::-1])
print(dizi[10:2:-1])

metin = "Balıkesir"
print(metin[::-1])

m = list(metin)
random.shuffle(m)
print(m)
