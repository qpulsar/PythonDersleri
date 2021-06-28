# dizi içinde tekrar eden elemanların yok edilmesi

dizi = [5, 6, 7, 6, 7, 8, 3, 3, 1, 8]

temiz = []
for i in dizi:
    if i not in temiz:
        temiz.append(i)

print(temiz)
