while True:
    user_input = input("Enter a command (type 'quit' to exit): ").strip().lower()
    
    if user_input == 'quit':
        print("👋 Bye bye! Closing the application...")
        break  # Safely breaks out of the loop
        
    print(f"Executing: {user_input}")
