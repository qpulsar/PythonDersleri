# Dizinin elemanlarının sırasını ters çeviren programı yazınız
sayilar = [1, 4, 3, 5, 1, 3, 7, 11]

print(sayilar[::-1])
ters = []
for i in range(len(sayilar)-1, -1, -1):
    ters.append(sayilar[i])

print(ters)

