# Define two integers
a = 12  # In binary: 1100
b = 10  # In binary: 1010

# 1. Bitwise AND (&) - Sets bit to 1 if both bits are 1
print(f"a & b = {a & b}  (Binary: {bin(a & b)})")  # Output: 8 (1000)

# 2. Bitwise OR (|) - Sets bit to 1 if at least one bit is 1
print(f"a | b = {a | b} (Binary: {bin(a | b)})")  # Output: 14 (1110)

# 3. Bitwise XOR (^) - Sets bit to 1 if only one of the bits is 1
print(f"a ^ b = {a ^ b}  (Binary: {bin(a ^ b)})")  # Output: 6 (0110)
