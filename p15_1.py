num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))

if num1 > num2 and num1 > num3:
    print(f"The greatest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The greatest number is {num2}")
else:
    print(f"The greatest number is {num3}")