# Input student score
score = float(input("Enter the student's score (0-100): "))

# Determine the letter grade using conditional blocks
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 0 and score < 60:
    grade = "F"
else:
    grade = "Invalid Score"

print(f"Grade: {grade}")
