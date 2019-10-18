def kdv(fiyat, oran=18):
    sonuc = fiyat * oran / 100
    return sonuc


def ikiKat_ve_Yarisi(bir, iki):
    return bir * 2, iki / 2


print("100TL'nin kdv'si = ", kdv(100))
print("50TL'nin kdv'si = ", kdv(50, 8))

elmakdv = kdv(2.5, 3)
us = pow(5, 2)
print("elma", elmakdv)

a, b = ikiKat_ve_Yarisi(50,40)
print(a,b)
