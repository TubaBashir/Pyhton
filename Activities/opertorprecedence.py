# Expression 1: Multiplication happens before addition
# 5 + (3 * 2) = 5 + 6 = 11
result1 = 5 + 3 * 2
print(f"5 + 3 * 2 = {result1}")

# Expression 2: Parentheses override normal precedence
# (5 + 3) * 2 = 8 * 2 = 16
result2 = (5 + 3) * 2
print(f"(5 + 3) * 2 = {result2}")

# Expression 3: Exponents (**) happen before multiplication (*)
# 2 * (3 ** 2) = 2 * 9 = 18
result3 = 2 * 3 ** 2
print(f"2 * 3 ** 2 = {result3}")
