"""
fibonacci dizisini bulan program
1,1,2,3,5,8,13,21...
"""
"""
limit = 50
s1 = 1
s2 = 1
for i in range(100):
    temp = s1 + s2
    s1 = s2
    s2 = temp
    print(s2)

# daha kısa yöntem
a, b = 1, 1
print(a)
print(b)
i = 2
while i <= 100:
    a, b = b, a + b
    print(b)
    i += 1
"""
#dizi
fi = [2, 3, 5]
for i in range(50):
    fi += [fi[len(fi)-1] + fi[len(fi)-2]]

print(fi)
