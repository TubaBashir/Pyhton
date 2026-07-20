print("💬 Chat system active. Type 'exit' to quit.")

while True:
    user_input = input("Enter a message: ").strip()
    
    # Check if the user wants to leave
    if user_input.lower() == 'exit':
        print("👋 Exiting the program. Goodbye!")
        break  # Instantly terminates the loop
        
    print(f"Echo: {user_input}")
