"""
Çık yazıncaya kadar girilen kelimeri dosyaya yazan programı yazınız
"""

devam = True
dosya = open("kelime.txt", "a")

while devam:
    kelime = input("Kelime :")
    dosya.write(kelime+"\n")
    if kelime == "Çık":
        devam = False

dosya.close()



