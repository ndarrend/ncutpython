upper_bound = int(input("Give me a big integer:"))
plist = []
for i in range(1, upper_bound + 1):
    for j in range(1, upper_bound + 1):
        for k in range(1, upper_bound +1):
            if k*k == i*i + j*j:
                plist.append((i,j,k))
print(plist)
for i in plist:
    print(i)