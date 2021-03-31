"""
*     *
 *   *
  * *
  * *
 *   *
*     *
"""
for satir in range(1, 4):
    print((satir - 1) * " ", "o", sep='', end='')
    print((7 - satir*2) * " ", "o", sep='')
for satir in range(3, 0, -1):
    print((satir - 1) * " ", "o", sep='', end='')
    print((7 - satir*2) * " ", "o", sep='')
