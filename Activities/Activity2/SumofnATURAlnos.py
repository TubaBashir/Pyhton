def sum_of_natural_numbers(n):
    # Using integer division (//) ensures the result is an integer
    return (n * (n + 1)) // 2

# Example usage: Sum of numbers from 1 to 100
n = 100
print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers(n)}")
# Output: 5050
