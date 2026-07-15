# Get user input for the total number of rows
rows = int(input("Enter the number of rows: "))

print("\nMirrored Right-Angled Triangle:")
# Loop through each row from 1 to the total number of rows
for i in range(1, rows + 1):
    # Print leading spaces (decreases each row)
    print(" " * (rows - i), end="")
    # Print stars (increases each row)
    print("*" * i)
