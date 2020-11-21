# 4 işlem programı

print("--- MENÜ ---")
print("1- Toplama")
print("2- Çıkarma")
print("3- Bölme")
print("4- Çarpma")
secim = input("Seçiminiz -->")
if secim == "1":
    print("Toplama")
    print(10*"-")
    sayi1 = float(input("1. Sayıyı giriniz :"))
    sayi2 = float(input("2. Sayıyı giriniz :"))
    sonuc = sayi1 + sayi2
    print(f"{sayi1}+{sayi2}={sonuc}")
elif secim == "2":
    print("Çıkarma")
    print(10*"-")
    sayi1 = float(input("1. Sayıyı giriniz :"))
    sayi2 = float(input("2. Sayıyı giriniz :"))
    sonuc = sayi1 - sayi2
    print(f"{sayi1}-{sayi2}={sonuc}")
elif secim == "3":
    print("Bölme")
    print(10*"-")
    sayi1 = float(input("1. Sayıyı giriniz :"))
    sayi2 = float(input("2. Sayıyı giriniz :"))
    if(sayi2==0):
        print("Tanımsız")
        exit()  # programı sonlandır
    bolum = sayi1 // sayi2
    kalan = sayi1 % sayi2
    print(f"{sayi1}/{sayi2}={bolum}")
    print(f"kalan = {kalan}")
elif secim == "4":
    print("Çarpma")
    print(10*"-")
    sayi1 = float(input("1. Sayıyı giriniz :"))
    sayi2 = float(input("2. Sayıyı giriniz :"))
    sonuc = sayi1 * sayi2
    print(f"{sayi1}*{sayi2}={sonuc}")
else:
    print("Hatalı seçim")
