a = float(input("Input first side: "))
b = float(input("Input second side: "))
c = float(input("Input third side: "))

if a + b > c and a + c > b and b + c > a:
    
    if a == b and b == c:
        print("The triangle is Equilateral.")
    elif a == b or a == c or b == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The triangle is not valid.")