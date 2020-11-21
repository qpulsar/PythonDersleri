"""
satır sayısı verilen üçgeni * kullanarak yazan fonksiyonu yapınız
ucgen_yildiz(3)
:
*
**
***
"""


def ucgen_yildiz(satir):
    for i in range(1, satir + 1):
        print(i * "*")


ucgen_yildiz(5)
