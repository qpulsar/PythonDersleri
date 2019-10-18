sayac = 1
ys = 1
artis = 2


while sayac<22:
    print("{:^25}".format(ys*"*"))
    ys += artis
    if sayac==10:
        artis = -2;
    sayac += 1