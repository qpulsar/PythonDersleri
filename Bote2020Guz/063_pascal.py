"""
Pascal üçgenini yazdırınız
1
1 1
1 2 1
1 3 3 1
"""

satir_sayisi = 5
ucgen = [1]
for i in range(satir_sayisi):
    print(ucgen)
    yeni_satir = []
    yeni_satir.append(ucgen[0])
    for k in range(len(ucgen) - 1):
        yeni_satir.append(ucgen[k] + ucgen[k + 1])
    yeni_satir.append(ucgen[-1])
    ucgen = yeni_satir

print(ucgen)
