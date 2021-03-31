sayi = 43
mesaj = "ASAL"
for i in range(2, sayi):
    if sayi % i == 0:
        mesaj = "asal değil"
        break


print(mesaj)

