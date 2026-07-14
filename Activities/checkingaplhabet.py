# Input from the user
user_input = input("Enter a single character or text: ")

# Check if the input consists only of alphabetic letters
if user_input.isalpha():
    print(f"'{user_input}' contains only alphabet letters.")
else:
    print(f"'{user_input}' contains numbers, spaces, or symbols.")
