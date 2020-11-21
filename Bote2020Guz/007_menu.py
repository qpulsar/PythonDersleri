print("---MENÜ---")
print("1- Dairenin alanı")
print("2- Dikdörtgenin alanı")
secim = int(input("Seçiminiz :"))

if secim == 1:
    print("DAİRE")
    r = float(input("Yarıçapı giriniz:"))
    print("Alan = {}".format(3.14 * pow(r, 2)))
elif secim == 2:
    print("DİKDÖRTGEN")
    a = float(input("Birinci kenarı giriniz:"))
    b = float(input("İkinci kenarı giriniz:"))
    alan = a * b
    print(f"Alan={alan}")
    # print("Alan={}".format(alan))
else:
    print("Yanlış seçim")
