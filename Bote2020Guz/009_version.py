import sys

print(sys.version_info)
print(sys.version_info.major)

if sys.version_info.major <3:
    print("Python'ın son sürümünü kullanırsanız çok daha iyi olur.")
else:
    print("Sıkıntı yok!")
