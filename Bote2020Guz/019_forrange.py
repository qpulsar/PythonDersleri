okul = "Balıkesir Üniversitesi Necatibey Eğitim Fakültesi"

for harf in okul:
    print(2 * harf)

var = "Ç" in okul
print(var)

turkce = "ÜĞİŞÇÖüğışçö"

for th in turkce:
    if th in okul:
        print(f"{th} var")
    else:
        print(f"{th} yok")

i = 0
while i < len(turkce):
    th = turkce[i]
    if th in okul:
        print(f"{th} var")
    else:
        print(f"{th} yok")

    i += 1

for th in turkce:
    if not th in okul:
        print(f"{th} yok")
    else:
        print(f"{th} var")
