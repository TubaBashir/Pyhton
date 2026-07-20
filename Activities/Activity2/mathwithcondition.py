def apply_conditional_math(num):
    # Condition 1: If the number is negative, square it
    if num < 0:
        result = num ** 2
        operation = "Squared (Negative Input)"
    
    # Condition 2: If the number is even, divide it by 2
    elif num % 2 == 0:
        result = num / 2
        operation = "Halved (Even Input)"
    
    # Condition 3: If the number is odd and positive, multiply by 3
    else:
        result = num * 3
        operation = "Tripled (Odd Input)"
        
    return result, operation

# Example usage:
for test_val in [-4, 10, 7]:
    res, op = apply_conditional_math(test_val)
    print(f"Input: {test_val:2d} -> {op:25s} -> Result: {res}")
