def find_midproduct(number):
    # Convert number to string to easily access indices
    num_str = str(abs(number))
    length = len(num_str)
    
    # Handle single digit numbers directly
    if length == 1:
        return int(num_str)
    
    # Determine the middle indices
    mid = length // 2
    
    if length % 2 != 0:
        # Odd length: Exactly one middle digit
        mid_digits = [int(num_str[mid])]
    else:
        # Even length: Two middle digits
        mid_digits = [int(num_str[mid - 1]), int(num_str[mid])]
    
    # Calculate the product of the extracted middle digits
    product = 1
    for digit in mid_digits:
        product *= digit
        
    return product

# --- Example Usage ---
print(find_midproduct(12345))  # Odd length: Middle digit is 3 -> Result: 3
print(find_midproduct(4567))   # Even length: Middle digits are 5 and 6 -> 5 * 6 -> Result: 30
