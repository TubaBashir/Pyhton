def decimal_to_binary_manual(n):
    if n == 0:
        return "0"
        
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2  # Floor division to reduce the number
        
    # The remainders are collected in reverse order, so we flip the list
    binary_digits.reverse()
    return "".join(binary_digits)

# Example usage:
number = 25
print(f"The binary of {number} is: {decimal_to_binary_manual(number)}")  # Output: 11001
