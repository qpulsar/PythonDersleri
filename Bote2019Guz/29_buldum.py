mesaj = input("Bir metin giriniz:")

kontrol = "ÜĞİŞÇÖüğışçö"
bulundu = False

for i in kontrol:
    if i in mesaj:
        print("Türkçe karakter var gülüm")
        bulundu = True
        break

if bulundu == False:
    print("Eyvallah hiç bir şey yok")
