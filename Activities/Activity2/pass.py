try:
    # Attempting to convert an invalid text input to an integer
    value = int("NotANumber")
except ValueError:
    pass  # Silently ignore the error and keep moving forward

print("The program successfully continued running!")
