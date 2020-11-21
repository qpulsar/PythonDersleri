"""
Text dosyası ile rehber programı
"""

DOSYA_ADI = "./rehber.dat"
rehber = None


def herseyi_oku():
    global dosya, rehber
    dosya = open(DOSYA_ADI, "r")
    dosya.seek(0)  # dosyanın en başına git
    rehber = dosya.readlines()
    print(rehber)
    dosya.close()


def kayit():
    global rehber
    dosya = open(DOSYA_ADI, "a")
    print(10 * "-" + "YENİ KAYIT" + 10 * "-")
    isim = input("Kişinin ismi :")
    telefon = input("Telefon :")
    insta = input("Instagram :")
    rehber.append([isim, telefon, insta])
    dosya.write(isim + "\t" + telefon + "\t" + insta + "\n")
    dosya.close()
    print(rehber)


def menu():
    while True:
        print("MENÜ")
        print("1-Kayıt")
        print("2-Liste")
        print("3-Ara")
        print("4-Düzelt")
        print("5-Sil")
        print("6-Çıkış")
        secim = int(input("Seçiminiz : "))
        if secim > 0 and secim < 7:
            return secim
        else:
            print("Seçiminiz 1..6 arasında olmalı!")


def listele():
    global rehber
    print("{:20}{:15}{:20}".format("İsim", "Telefon", "Instagram"))
    print(55 * "_")
    for kisi in rehber:
        bilgi = kisi.split("\t")
        print("{:20}{:15}{:20}".format(bilgi[0], bilgi[1], bilgi[2].strip()))

    input("Enter'a basınız...")


def ara():
    global rehber
    print("Aramak istediğiniz bilgi:")
    print("1- İsim")
    print("2- telefon")
    print("3- Instagram")
    t = int(input("seciminiz:"))
    if t == 1:
        i = input("aradığınız ismi giriniz:")
        for kisi in rehber:
            b = kisi.split("\t")
            if b[0] == i:
                print("{:20}{:15}{:20}".format(b[0], b[1], b[2].strip()))
    elif t == 2:
        i = input("aradığınız telefonu giriniz:")
        for kisi in rehber:
            b = kisi.split("\t")
            if b[1] == i:
                print("{:20}{:15}{:20}".format(b[0], b[1], b[2].strip()))
    elif t == 3:
        i = input("aradığınız Instagramı giriniz:")
        for kisi in rehber:
            b = kisi.split("\t")
            if b[2].strip() == i:
                print("{:20}{:15}{:20}".format(b[0], b[1], b[2].strip()))

    input("Menüye dönmek için Enter'a basınız...")


def duzelt():
    global rehber
    i = input("Düzeltme yapılacak ismi giriniz:")
    satir = 0
    for kisi in rehber:
        b = kisi.split("\t")
        if b[0] == i:
            print("{:20}{:15}{:20}".format(b[0], b[1], b[2].strip()))
            bumu = input("Düzeltme yapılacak kayıt bu mu? (E/H):")
            if bumu.upper() == "E":
                dosya = open(DOSYA_ADI, "w")
                print(10 * "-" + "KAYIT DÜZELTME" + 10 * "-")
                isim = input("Kişinin ismi :")
                telefon = input("Telefon :")
                insta = input("Instagram :")
                rehber[satir] = isim + "\t" + telefon + "\t" + insta + "\n"
                dosya.write("".join(rehber))
                dosya.close()
        satir += 1


def sil():
    global rehber
    i = input("Silinecek yapılacak ismi giriniz:")
    satir = 0
    for kisi in rehber:
        b = kisi.split("\t")
        if b[0] == i:
            print("{:20}{:15}{:20}".format(b[0], b[1], b[2].strip()))
            bumu = input("Silinecek kayıt bu mu? (E/H):")
            if bumu.upper() == "E":
                dosya = open(DOSYA_ADI, "w")
                print(10 * "-" + "KAYIT Silinecek" + 10 * "-")
                rehber.pop(satir)
                dosya.write("".join(rehber))
                dosya.close()
        satir += 1


if __name__ == '__main__':
    herseyi_oku()
    while True:
        secim = menu()
        if secim == 1:
            kayit()
        elif secim == 2:
            listele()
        elif secim == 3:
            ara()
        elif secim == 4:
            duzelt()
        elif secim == 5:
            sil()
        elif secim == 6:
            kesin = input("Çıkmak istediğinize emin misiniz(E/H):")
            if kesin == 'e' or kesin == 'E':
                print("Yine bekleriz...")
                dosya.close()
                exit(99)
