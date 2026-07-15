# Get user input for the size of the square
size = int(input("Enter the side length of the square: "))

print("\nSolid Square:")
# Outer loop for rows
for i in range(size):
    # Inner loop for columns
    for j in range(size):
        print("* ", end="")
    # Move to the next line after completing a row
    print()
