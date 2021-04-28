dosya = open("029_list.py", "r", encoding="utf8")  # war

print(dosya.read())

print(40 * "-")
dosya.seek(0) # dosyanın en başına git
print(dosya.readline(), end="")
print(dosya.readline(), end="")

dosya.seek(0)
satirlar = dosya.readlines()
print(satirlar)
