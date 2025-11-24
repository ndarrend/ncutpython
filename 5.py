bmi= float(input("Enter BMI:"))
category = 'Normal' if bmi < 25 else(
'Overweight' if bmi<29.9 else 'Obese'
)
print(f"Category:{category}")