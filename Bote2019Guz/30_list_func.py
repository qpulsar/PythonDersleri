dizi = ["Gül","Lale"]

print(dizi)

dizi.append("Menekşe")
print(dizi)

dizi.extend(["Mum çiçeği", "sümbül"])
print(dizi)

dizi.insert(3, "Orkide")
print(dizi)

dizi.remove("Menekşe")
print(dizi)

dizi.pop()
print(dizi)

print(dizi.count("Orkide"))

dizi.sort()
print(dizi)

dizi.sort(key=len, reverse=True)
print(dizi)

print(len(dizi))

