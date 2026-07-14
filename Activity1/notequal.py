# Input a secret password guess
correct_password = "python123"
user_guess = input("Enter the password: ")

# Check if the guess is NOT EQUAL to the correct password
if user_guess != correct_password:
    print("Access Denied: Incorrect password.")
else:
    print("Access Granted: Welcome!")
