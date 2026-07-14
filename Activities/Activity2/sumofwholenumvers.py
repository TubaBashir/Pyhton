# Input how many whole numbers to sum
n = int(input("Enter how many whole numbers to sum (N): "))

if n <= 0:
    print("Please enter a number greater than 0.")
else:
    # Method 1: Using a simple math formula: (n * (n - 1)) / 2
    # Whole numbers start at 0, so the first N numbers are 0 up to N-1
    total_sum = (n * (n - 1)) // 2
    
    print(f"The sum of the first {n} whole numbers is: {total_sum}")
