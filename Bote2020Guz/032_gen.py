dizi = [i * 2 for i in range(250) if i % 3 == 0]
print(dizi)

d = []
for i in range(250):
    if i % 3 == 0:
        d += [i * 2]
