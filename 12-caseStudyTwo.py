for i in range (1, 10):
    for j in range (1, 10):
        print(f"{i}x{j} = {i * j}", end = " ")
    print("\n")
print ("--------------------------------------------------------")
for i in range (1, 10):
    for j in range (1, 10):
        if j <= i:
            print(f"{i}x{j} = {i * j}", end = " ")
    print("\n")
print ("--------------------------------------------------------")
for i in range (1, 10):
    for j in range (1, i + 1):
        print(f"{i}x{j} = {i * j}", end = " ")
    print("\n")