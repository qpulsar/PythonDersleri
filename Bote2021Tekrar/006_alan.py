"""
Karenin alanını bulan program
Emin
24.03.2021
"""

kenar = float(input("Karenin bir kenarının uzunluğunu giriniz: "))
alan = pow(kenar, 2)  # kenar * kenar
print("karenin alanı = ", alan)
print("kenarı", kenar, "cm olan karenin alanı", alan, "cm karedir.")
print("kenarı {0}cm olan karenin alanı {1}cm karedir.".format(kenar, alan))
print(f"kenarı {kenar}cm olan karenin alanı {alan}cm karedir.")
