# dizinin en küçük elemanı

dizi = [5, 6, 7, 6, 7, 8, 3, 3, 1, 8]

ek = dizi[0]
for i in dizi[1:]:
    if i < ek:
        ek = i
print("en küçük:", ek)
