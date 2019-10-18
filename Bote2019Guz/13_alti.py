#3'e ve 2'ye bölünen sayıları listeleyin
#3'e veya 2'ye bölünen sayıları listeleyin

for i in range(1,100):
    if i%3==0 and i%2==0:
        print(i)

for i in range(1,100):
    if i%3==0 or i%2==0:
        print(i)