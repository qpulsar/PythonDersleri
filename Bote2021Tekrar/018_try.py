sayi1 = 34
sayi2 = 0

try:
    sonuc = sayi1 / sayi2
    print(sonuc)
except ZeroDivisionError:
    print("Sıfıra bölme hatası oluştu")
except:
    print("Ne yapsam olmadı")
finally:
    print("Ben her zaman çalışırım.")
