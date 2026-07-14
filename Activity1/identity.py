# Create two distinct lists with identical values
list_a = [1, 2, 3]
list_b = [1, 2, 3]

# Assign list_a to a new variable (they point to the exact same object)
list_c = list_a

# 1. Using '==' vs 'is'
print(f"Are values equal (list_a == list_b)? {list_a == list_b}")  # True
print(f"Are they the same object (list_a is list_b)? {list_a is list_b}")  # False

# 2. Using 'is' with a reference copy
print(f"Are they the same object (list_a is list_c)? {list_a is list_c}")  # True

# 3. Using 'is not'
print(f"Are they different objects (list_a is not list_b)? {list_a is not list_b}")  # True
