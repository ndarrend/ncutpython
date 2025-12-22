principal = float(input("Enter initial investment amount: "))
rate = float(input("Enter annual interest rate (%): ")) / 100
years = int(input("Enter number of years: "))

balance = principal
total_interest = 0.0

# Table header
print(f"\n{'Year':<6}{'Balance':>15}{'Interest Earned':>20}{'Total Interest':>20}")
print("-" * 61)

for year in range(1, years + 1):
    previous_balance = balance
    balance = balance * (1 + rate)

    interest_earned = balance - previous_balance
    total_interest += interest_earned

    print(f"{year:<6}" f"${balance:>14,.2f}"f"${interest_earned:>19,.2f}"f"${total_interest:>19,.2f}")