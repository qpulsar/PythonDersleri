"""
   *      *      *      *      *
  ***    ***    ***    ***    ***
 *****  *****  *****  *****  *****
"""
for i in range(1, 10, 2):
    for j in range(1, 6):
        print("{:^12}".format(i*"*"), end='')
    print()
