"""
Tersinden ve düzünden aynı okunan kelime girilinceye kadar
yeni kelime isteyen programı yazınız
palindrom
pop *
ütü
nalan
"""
kelime = None
while True:
    kelime = input("Öyle bir kelime giriniz:")
    if kelime == kelime[::-1]:
        break

