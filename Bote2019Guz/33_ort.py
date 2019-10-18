#20 elemanlı, 0-50 arası rastgele sayılarından olsuşan dizi
#dizinin toplamı
#dizinin ortalaması
#Her elemanın ortalamadan farkını yazdırın
import random

dizi = []
for i in range(0,20):
    dizi.append(random.randrange(0,50))

print(dizi)
print("Toplam = ",sum(dizi))
ortalama = round(sum(dizi)/len(dizi),2)
print("Ortalama = ",ortalama)

for i in dizi:
    print("{:>5} \t {:>5}".format(i, round(ortalama-i,2)))


