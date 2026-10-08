import hashlib
import os

USER_DATA_FILE = "users.txt"

def hash_password(password):
    """Convert a plain text password into a secure SHA-256 hash."""
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    """Register a new user and save their credentials securely."""
    print("\n--- REGISTER ---")
    username = input("Create Username: ").strip()
    password = input("Create Password: ").strip()
    
    if not username or not password:
        print("Username and password cannot be empty.")
        return

    hashed_pw = hash_password(password)

    # Check if the username already exists
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            for line in f:
                stored_user, _ = line.strip().split(",")
                if stored_user == username:
                    print("Username already exists! Try logging in.")
                    return

    # Append new user credentials to the file
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{hashed_pw}\n")
    print("Registration successful!")

def login():
    """Authenticate an existing user."""
    print("\n--- LOGIN ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not os.path.exists(USER_DATA_FILE):
        print("No users registered yet. Please register first.")
        return False

    hashed_input_pw = hash_password(password)

    # Verify credentials against stored records
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            stored_user, stored_hash = line.strip().split(",")
            if stored_user == username and stored_hash == hashed_input_pw:
                print(f"\nLogin Successful! Welcome, {username}.")
                return True
                
    print("\nInvalid username or password.")
    return False

def main():
    """Main program loop."""
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1, 2, or 3.")

if __name__ == "__main__":
    main()
