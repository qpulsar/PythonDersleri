try:
    dosya = open("043_write.py", "r")
    print(dosya.read())
    dosya.close()
except IOError:
    print("Dosyayı açarken bir hata oluştu.")
finally:
    print("Hatasıyla sevabıyla bir try'ın daha sonuna geldik.")
