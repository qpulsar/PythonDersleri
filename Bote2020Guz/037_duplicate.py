# dizide tekrar eden eleman kalmasın
sayilar = [1, 4, 3, 5, 1, 3, 7, 11]

yeni = []
for i in sayilar:
    if i not in yeni:
        yeni.append(i)

print(yeni)
