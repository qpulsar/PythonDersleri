dosya = open("044_try.py", "r")
dosya.seek(6)
print(dosya.readline())
dosya.seek(18)
print(dosya.readline())
print(dosya.tell()) #şu anda dosyanın kaçıncı byte'ındayım
