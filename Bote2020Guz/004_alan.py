"""
Dairenin alanını bulan program
Emin
19.10.2020
"""

r = float(input("Dairenin yarı çapını giriniz:"))
alan = 3.14 * r * r

print("alan = ", alan)
print("yarı çapı", r, "olan dairenin alanı", alan, "cm karedir")
print("yarı çapı {} olan dairenin alanı {} cm karedir".format(r, alan))
print(f"yarı çapı {r} olan dairenin alanı {alan} cm karedir")

