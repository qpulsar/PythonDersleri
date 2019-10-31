# palindrom kelime buluncaya kadar devam edeb program
while 1:
    metin = input("Kelimeyi girniniz :")
    print("{} : {}".format(metin, metin[::-1]))
    if metin == metin[::-1]:
        break
