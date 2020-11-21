sayi1 = 30
sayi2 = 0

try:
    sonuc = sayi1 / sayi2
    print(sonuc)
except ZeroDivisionError:
    print("Sıfıra bölme yapılamaz")
except:
    print("Olmuyor :(")
finally:
    print("Her şeye rağmen")

