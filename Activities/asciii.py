# 1. Get the ASCII value of a character (Character -> Number)
char = input("Enter a single character: ")
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")

# 2. Get the character from an ASCII value (Number -> Character)
code = int(input("\nEnter an ASCII number (e.g., 65): "))
character = chr(code)
print(f"The character for ASCII code {code} is '{character}'")
