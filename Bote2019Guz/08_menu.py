print("MENÜ")
print("1- Dairenin alanı")
print("2- Dikdörtgenin alanı")
secim = int(input("Seçiminiz :"))

if secim==1:
    r = float(input("Yarıçapı giriniz:"))
    print("Dairenin alanı {} ".format(3.14*r*r))
elif secim==2:
    a = float(input("Birinci kenarı giriniz:"))
    b = float(input("İkinci kenarı giriniz:"))
    print("Dikdörtgenin alanı {} ".format(a*b))
else:
    print("Yanlış seçim")
