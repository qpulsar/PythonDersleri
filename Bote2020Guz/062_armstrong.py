"""
Tüm basamaklarındaki rakamların sayı değerlerinin küpleri toplamı,kendisine eşit olan sayılara "Armstrong sayı"denir.
Verilen sayının armstrong sayısı olup olmadığın bulan fonksiyonu yazınız.
1634 -> 4 basamaklı
1 ^ 4 = 4
6 ^ 4 = 1296
3 ^ 4 = 81
4 ^ 4 = 256
"""


def armstrong_mu(sayi):
    str_sayi = str(sayi)
    basamak = len(str_sayi)
    toplam = 0
    for s in str_sayi:
        toplam += int(s)**basamak

    if sayi == toplam:
        return True
    else:
        return False


print(armstrong_mu(1634))  # True
print(armstrong_mu(2500))  # False
