income = float(input("Enter your taxable income: "))

total_tax = 0

if income > 48534:
    total_tax += 48534 * 0.15
    income -= 48534
else:
    total_tax += income * 0.15
    income = 0

if income > 48534:
    total_tax += 48534 * 0.205
    income -= 48534
else:
    total_tax += income * 0.205
    income = 0

if income > 0:
    total_tax += income * 0.26

print("Total tax owed: $", round(total_tax, 2))