number_grade = round(float(input("Enter grade between 0-100:")))

if number_grade >= 90:
    print(f"Letter grade for {number_grade}%is A+")
elif number_grade >= 85:
    print(f"Letter grade for {number_grade}% is A")
elif number_grade >= 80:
    print(f"Letter grade for {number_grade}% is A-")
elif number_grade >= 76:
    print(f"Letter grade for {number_grade}% is B+")
elif number_grade >= 73:
    print(f"Letter grade for {number_grade}% is B")
elif number_grade >= 70:
    print(f"Letter grade for {number_grade}% is B-")
elif number_grade >= 67:
    print(f"Letter grade for {number_grade}% is C+")
elif number_grade >= 64:
    print(f"Letter grade for {number_grade}% is C")
elif number_grade >= 60:
    print(f"Letter grade for {number_grade}% is C-")
elif number_grade >= 55:
    print(f"Letter grade for {number_grade}% is D+")
elif number_grade >= 50:
    print(f"Letter grade for {number_grade}% is D")
elif number_grade >= 0:
    print(f"Letter grade for {number_grade}% is F")
else:
    print("Numeric grade must be a positive integer")