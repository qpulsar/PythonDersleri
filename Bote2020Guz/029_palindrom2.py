"""
Tersinden ve düzünden aynı okunan kelime girilinceye kadar
yeni kelime isteyen programı yazınız
palindrom
pop *
ütü
nalan
"""
kelime = []
while len(kelime) <2 or kelime != kelime[::-1]:
    kelime = input("Tersi düzü aynı olsun :")
