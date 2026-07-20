def cube_of_cube_operators(num):
    # Method 1: Using the standard exponent operator (**) twice
    # This evaluates as (num ** 3) ** 3
    return (num ** 3) ** 3

def cube_of_cube_math(num):
    # Method 2: Evaluating it directly as the 9th power
    return num ** 9

def cube_of_cube_pow(num):
    # Method 3: Using Python's built-in pow() function
    return pow(pow(num, 3), 3)

# Example usage:
number = 2

print(f"Using operators: The cube of the cube of {number} is {cube_of_cube_operators(number)}")
print(f"Using 9th power: The cube of the cube of {number} is {cube_of_cube_math(number)}")
print(f"Using pow():     The cube of the cube of {number} is {cube_of_cube_pow(number)}")
