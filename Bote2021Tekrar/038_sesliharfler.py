def sesli_harfler(metin):
    sh = "aeıiuüoö"
    geri = []
    for harf in metin:
        if harf in sh:
            geri.append(harf)

    return geri


def sessiz_harfler(metin):
    sh = "aeıiuüoö"
    geri = []
    for harf in metin:
        if harf not in sh:
            geri.append(harf)

    return geri


bunubul = "Python sesli harfleri bulan fonksiyon örneği hayırlı uğurlu olsun."

sesli = sesli_harfler(bunubul)
print(sesli)
print(sessiz_harfler(bunubul))
