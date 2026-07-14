# Input two numbers
numerator = int(input("Enter the number to check (numerator): "))
denominator = int(input("Enter the divisor (denominator): "))

# Ensure we don't divide by zero
if denominator == 0:
    print("Error: Division by zero is not allowed.")
# Check divisibility using the remainder operator
elif numerator % denominator == 0:
    print(f"Yes! {numerator} is divisible by {denominator}.")
else:
    print(f"No! {numerator} is not divisible by {denominator}. Remainder is {numerator % denominator}.")
