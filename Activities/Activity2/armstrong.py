def is_armstrong(number):
    # Convert to string to easily count digits and iterate
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of num_digits
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum matches the original number
    return digit_sum == number

# Example usage:
test_num = 153
if is_armstrong(test_num):
    print(f"{test_num} is an Armstrong number!")
else:
    print(f"{test_num} is NOT an Armstrong number.")
# Output: 153 is an Armstrong number!
