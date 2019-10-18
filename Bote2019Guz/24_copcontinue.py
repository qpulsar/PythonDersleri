for i in range(1,10):
    for j in range(1,5):
        if j == 2:
            continue
        print(j, end="-")
    if i==5:
        print()
        continue
    print(f"**{i}")

