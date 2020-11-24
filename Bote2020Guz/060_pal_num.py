"""
Verilen bir sayının en az 3 basamaklı olması şartını kontrol eden ve
şart sağlanıyorsa sayının tersi ve düzünün aynı olması durumunda true döndüren fonksiyonu yazınız
"""


def pal_num(sayi):
    if int(sayi) < 100:
        return False

    s = str(sayi)
    if s == s[::-1]:
        return True
    else:
        return False


print(pal_num(265))
print(pal_num(262))
