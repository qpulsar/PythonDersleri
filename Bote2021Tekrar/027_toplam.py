# dizi elemanlarının toplanı bulan program

dizi = [5, 6, 7, 6, 7, 8, 3, 3, 1, 8]

toplam = 0
for i in dizi:
    toplam += i  # toplam = toplam + i

print("toplam =", toplam)
print("toplam =", sum(dizi))
