""" tekrar etmeyen 10 sayı rastgele 1-100 arasında"""
import random

sayilar = []
maks = 100
for i in range(10):
    sayi = random.randrange(1, maks)
    while sayi in sayilar:
        print("aynısı geldi bi daha atıyorum")
        sayi = random.randrange(1, maks)

    sayilar += [sayi]

print(sayilar)

