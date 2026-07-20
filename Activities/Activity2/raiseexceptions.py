def register_user(username, age):
    # Rule 1: Age must be a realistic positive number
    if age < 0:
        raise ValueError(f"Registration failed: Age cannot be negative (provided: {age}).")
    
    # Rule 2: Username cannot be blank
    if not username.strip():
        raise ValueError("Registration failed: Username cannot be empty.")
        
    print(f"✅ User '{username}' registered successfully!")

# Test the exception logic using a try-except block to catch the raised error
try:
    register_user("Alice", -5)
except ValueError as error:
    print(f"🚨 Caught an intentional error: {error}")
