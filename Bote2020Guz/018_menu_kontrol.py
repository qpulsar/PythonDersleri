secim = None
while secim != 3:
    print(*" MENÜ ", sep="_")
    print("1- Üssünü al")
    print("2- Üçgenin alanı")
    print("3- Programı sonlandır")
    secim = int(input("Seçiminiz :"))
    if secim == 1:
        sayi = int(input("tabanı giriniz:"))
        us = int(input("üssü giriniz:"))
        sonuc = sayi ** us
        print("{} ^ {} = {}".format(sayi, us, sonuc))
    elif secim == 2:
        taban = int(input("tabanı giriniz:"))
        h = int(input("yüksekliği giriniz:"))
        sonuc = taban * h / 2
        print("Üçgenin alanı = ", sonuc)

    elif secim == 3:
        karar = input("Çıkmak istiyorsanız 'E' tuşuna basınız:")
        if karar.upper() == "E":
            secim = 3
            print("Güle güle :)")
        else:
            secim = None
    else:
        print("Hatalı Seçim!!!")
