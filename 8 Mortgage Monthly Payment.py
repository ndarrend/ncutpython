principal = float(input("Enter the principal amount: "))

annual_rate = float(input("Enter the annual interest rate (%): "))
r = annual_rate / 100 / 12

years = int(input("Enter the number of years: "))
N = 12 * years

if r == 0:
    monthly_payment = principal / N
else:
    monthly_payment = principal * (r * (1 + r) ** N) / ((1 + r) ** N - 1)

print(f"Monthly mortgage payment: ${monthly_payment:,.2f}")