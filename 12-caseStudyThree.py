upper_bound = int(input ("Give me a big integer:"))
plist = []
for i in range (1, upper_bound + 1):
    for j in range (i, upper_bound + 1):
        for k in range (j, upper_bound + 1):
            if k * k == j * j + i * i:
                plist.append((i, j , k))
for i in plist:
    print (i)