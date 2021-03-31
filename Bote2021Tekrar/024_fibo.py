# 1, 1, 2, 3, 5, 8, 13, 21
fi = [1, 1, 2]
for i in range(50):
    fi += [fi[len(fi)-1]+fi[len(fi)-2]]

print(fi)
