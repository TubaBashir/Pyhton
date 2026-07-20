user_input = input("Enter your age: ").strip()

try:
    age = int(user_input)
    print(f"✅ Age recorded successfully: {age}")
except ValueError:
    print(f"❌ Input Error: '{user_input}' is not a valid number. Please enter digits only.")
