"""
Verilen bir metin içinde aranan harfin kaç tane olduğunu döndüren fonksiyonu yazınız
"""


def harf_say(str, aranan):
    sayac = 0
    for h in str:
        if h == aranan:
            sayac += 1
    return sayac


def duyarsiz_harf_say(str, aranan):
    sayac = 0
    for h in str:
        if h.upper() == aranan.upper():
            sayac += 1
    return sayac


metin = "Balıkesir Üniversitesi Necatibey Eğitim Fakültesi"
print(harf_say(metin, 'e'))
print(duyarsiz_harf_say(metin, 'e'))
