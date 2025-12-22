a = float(input("Input first side: "))
b = float(input("Input second side: "))
c = float(input("Input third side: "))

if a + b > c and a + c > b and b + c > a:

    longest = max(a, b, c)

    if longest == a:
        side1, side2 = b, c
    elif longest == b:
        side1, side2 = a, c
    else:
        side1, side2 = a, b

    if abs(side1**2 + side2**2 - longest**2) < 1e-6:
        print("The triangle is a Right triangle.")
    else:
        print("The triangle is not a Right triangle.")

else:
    print("The triangle is not valid.")