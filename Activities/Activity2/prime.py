def is_prime_easy(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
        
    # Check if any number from 2 up to (num - 1) divides it perfectly
    for i in range(2, num):
        if num % i == 0:
            return False  # Found a divisor, so it is not prime
            
    return True  # No divisors found, it is prime

# --- How to use it ---
number = 13

if is_prime_easy(number):
    print(f"{number} is a prime number!")
else:
    print(f"{number} is not a prime number.")
# Output: 13 is a prime number!
