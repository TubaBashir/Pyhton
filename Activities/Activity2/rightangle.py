def is_right_angle(s1, s2, s3):
    # Sort sides so the largest is always at index 2 (hypotenuse)
    sides = sorted([s1, s2, s3])
    
    # Check if a^2 + b^2 == c^2
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

print(is_right_angle(3, 4, 5))    # Output: True
print(is_right_angle(5, 12, 13))  # Output: True
print(is_right_angle(3, 3, 3))    # Output: False
