d = []
for i in range(1, 100):
    if i % 3 == 0:
        d.append(i * 2)

print(d)

e = [i*2 for i in range(1, 100) if i % 3 == 0]

print(e)
