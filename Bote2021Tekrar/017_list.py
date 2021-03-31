dizi = [5, 3, "herşey", 3.2, ["e", 7]]

print(dizi)
print(dizi[1])
print(dizi[4][0])

dizi[1] = 99
print(dizi[1])

dizi.append(99)
print(dizi)
print(20*"-")
for i in dizi:
    print(i)

for j in "Merhaba Dünya":
    print(j)

if "a" in "Merhaba Dünya":
    print("a bu metinde var.")
if "ö" in "Merhaba Dünya":
    print("ö bu metinde var.")
