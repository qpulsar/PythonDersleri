# En büyük elemanı bulan programı yazınız
sayilar = [1, 4, 3, 5, 1, 3, 7, 11]
print(max(sayilar))

eb = 0
for s in sayilar:
    if s > eb:
        eb = s
print("Benim bulduğum en büyük sayı:", eb)
