secim = None
while secim != 3:
    print("--- MENÜ ---")
    print("1- Daire")
    print("2- Kare")
    print("3- Çıkış")
    secim = int(input("Seçiminiz :"))

    if secim == 1:
        r = float(input("Yarı çapı giriniz:"))
        print("alan={}".format(3.14 * pow(r, 2)))
    elif secim == 2:
        kenar = float(input("Bir kenarı giriniz:"))
        print("alan={}".format(pow(kenar, 2)))
    elif secim == 3:
        print("Güle güle")
    else:
        print("Yanlış seçim")
