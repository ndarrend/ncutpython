n = int(input("Enter the number of terms: "))

pi_sum = 0

for i in range(n):
    term = (-1) ** i / (2 * i + 1)
    pi_sum += term

pi_approx = 4 * pi_sum

print("Approximation of π using", n, "terms is:", pi_approx)