"""
   *      *      *      *      *
  ***    ***    ***    ***    ***
 *****  *****  *****  *****  *****
"""
for i in range(1,6,2):
    for j in range(1,6):
        print("{:^7}".format(i*"*"), end="")
    print()