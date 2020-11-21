"""
Rehber programının yapısı
"""

def kaydet():
    pass


def listele():
    pass

def menu():
    print("MENÜ")
    print("1-Kayıt")
    print("2-Liste")
    print("3-Ara")
    print("4-Düzelt")
    print("5-Sil")
    print("6-Çıkış")
    secim = int(input("Seçiminiz :"))
    return secim

s = None
devam = True
while devam:
    s = menu()
    if s==6:
        sonuc = input("Çıkmak istediğinizden emin misiniz(E/H):")
        if sonuc.upper() == 'E':
            devam = False
            print("Güle güle")
        elif sonuc.upper() == 'H':
            devam = True
    elif s == 1:
        kaydet()
    elif s == 2:
        listele()
