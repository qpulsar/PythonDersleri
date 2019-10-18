""" Aşağıdaki çıktıyı veren programı yazınız
   2
 3 4
 6 8
 9 10
"""
print("\t", end="")
for i in range(1, 100):
    if i%3 == 0:
        print(i, end="\t")
    elif i%2 ==0:
        print(i)
