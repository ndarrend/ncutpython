a = float(input("Input first side: "))
b = float(input("Input second side: "))
c = float(input("Input third side: "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")