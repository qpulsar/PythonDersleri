# Verilen sayı asal mı?

sayi = 97
mesaj = "ASAL"
for i in range(2, sayi):
    if sayi % i == 0:
        mesaj = "Asal Değildir -> {}".format(i)
        break

print(mesaj)
