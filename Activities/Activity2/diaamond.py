# Get user input for the maximum width (must be odd for a perfect diamond)
rows = int(input("Enter number of rows (half of diamond height): "))

# Upper part of the diamond (including the center line)
for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print stars with spaces in between
    print("* " * i)

# Lower part of the diamond
for i in range(rows - 1, 0, -1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print stars with spaces in between
    print("* " * i)
