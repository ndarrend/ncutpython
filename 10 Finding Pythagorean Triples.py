upper = int(input("Enter the upper bound: "))

for a in range(1, upper + 1):
    for b in range(a, upper + 1):
        c_squared = a*a + b*b
        c = int(c_squared ** 0.5)

        if c <= upper and c*c == c_squared:
            print(a, b, c)