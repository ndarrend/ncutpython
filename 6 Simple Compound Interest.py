a = float(input("Input initial deposit: "))
b = float(input("Input annual interest rate (%): "))
c = float(input("Input number of years: "))

rate = b / 100

amount = a * (1 + rate) ** c

print("Final amount after", c, "years is:", round(amount, 2))