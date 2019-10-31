# 1. Diziye kelime eklesin
# 2. uzun kelimeden kısa kelimeye doğru sıralayarak yazsın
# 3. Kelimelerdeki toplam harf sayını bulup her keliminin ortalamadan farkını yazın
# 4. Sesli harflerini çıkartarak yeni bir diziye ekleyin ve yazdırın
# 5. Çıkış
# Birinci seçenek seçilmediyse 2-3-4 uyarı versin

def menu():
    print(10 * "*" + "M E N Ü" + 10 * "*")
    print("{:>3}- Kelime Ekle".format(1))
    print("{:>3}- Uzunluğa göre sırala".format(2))
    print("{:>3}- Ortalama harf sayısı".format(3))
    print("{:>3}- Sessiz harfler".format(4))
    print("{:>3}- Hadi bana eyvallah".format(5))
    secim = int(input("Seçiminiz :"))
    return secim


devam = True
bir_tamam = False
kelimeler = []
while devam:
    sec = menu()
    if sec == 1:
        bir_tamam = True
        kelimeler.append(input("Bir kelime giriniz:"))
    elif sec == 2:
        if bir_tamam == True:
            kelimeler.sort(key=len)
            print(kelimeler)
        else:
            print("Önce kelime eklemelsiniz...")
    elif sec == 3:
        if bir_tamam == True:
            toplam = 0
            for kelime in kelimeler:
                toplam += len(kelime)
            ortalama = toplam // len(kelimeler)
            for i in kelimeler:
                print("{}:{} > {}".format(i, len(i), len(i) - ortalama))
        else:
            print("Önce kelime eklemelsiniz...")
    elif sec == 4:
        if bir_tamam == True:
            sesli="AaEeIıİiÜüÖöOoUu"
            for kelime in kelimeler:
                for harf in kelime:
                    if harf in sesli:
                        pass
                    else:
                        print(harf, end="")
                print()
        else:
            print("Önce kelime eklemelsiniz...")
    elif sec == 5:
        c = input("Çıkmak istediğinize emin misiniz? (E/H)")
        if c.upper()=="E":
            print("Güle güle")
            devam = False
        elif c.upper()=="H":
            devam = True
        else:
            print("Geçersiz yanıt.")
    else:
        print("Seçiminiz 1-5 arasında olmalı.")

