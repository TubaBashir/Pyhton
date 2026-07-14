# Input the person's age
age = int(input("Enter age: "))

# Check if age meets the legal adulthood threshold
if age >= 18:
    print("Status: Adult (Eligible to vote/drive)")
elif age >= 0:
    print("Status: Minor (Under 18)")
else:
    print("Invalid Input: Age cannot be negative")
