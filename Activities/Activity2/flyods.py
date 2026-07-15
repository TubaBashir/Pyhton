# Get user input for the number of rows
rows = int(input("Enter the number of rows: "))

# Initialize the starting number
current_number = 1

print("\nFloyd's Triangle:")
# Outer loop handles the number of rows
for i in range(1, rows + 1):
    # Inner loop handles printing numbers in each row
    for j in range(1, i + 1):
        print(current_number, end=" ")
        current_number += 1  # Increment the counter
    
    # Move to the next line after completing a row
    print()
