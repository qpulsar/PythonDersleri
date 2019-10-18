"""
Verilen metinde Türkçe'ye özgü karakterlerden bulunup bulunmadığını belirleyiniz
"""
kontrol = "ÜĞİŞÇÖüğışçö"
metin = "Bugun hava guneşli ve güller harika kokuyor"
for harf in kontrol:
    if harf in metin:
        print(f"{harf} bulundu")
    else:
        print(f"{harf} bulamadım")

