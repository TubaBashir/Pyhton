# Input weight in kilograms and height in meters
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI (weight divided by height squared)
bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.1f}")

# Check BMI category based on standard thresholds
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")
