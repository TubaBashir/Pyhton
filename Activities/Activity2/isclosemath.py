import math

# Floating point example: 0.1 + 0.2 equals 0.30000000000000004 under the hood
a = 0.1 + 0.2
b = 0.3

# Direct comparison fails
print(a == b)  # Output: False

# Using math.isclose() succeeds
print(math.isclose(a, b))  # Output: True
