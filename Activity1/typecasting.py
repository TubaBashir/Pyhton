# 1. String to Integer
age_str = "25"
age_int = int(age_str)
print(age_int + 5)        # Output: 30

# 2. Integer to Float
score_int = 95
score_float = float(score_int)
print(score_float)        # Output: 95.0

# 3. Float to Integer (Truncates decimals)
pi_float = 3.99
pi_int = int(pi_float)
print(pi_int)             # Output: 3

# 4. Number to String (Useful for concatenation)
items = 3
message = "I bought " + str(items) + " apples."
print(message)            # Output: I bought 3 apples.
