import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("🎯 I'm thinking of a number between 1 and 100.")
    
    # 1. Generate a secret number and set up game parameters
    secret_number = random.randint(1, 100)
    attempts_left = 7
    
    print(f"⏰ You have {attempts_left} attempts to guess it right. Good luck!\n")
    
    # 2. Main game loop
    while attempts_left > 0:
        print(f"📊 Attempts remaining: {attempts_left}")
        user_input = input("Enter your guess: ").strip()
        
        # Validate that the input is a valid number
        try:
            guess = int(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")
            continue
            
        # Check if the guess is within the bounds
        if guess < 1 or guess > 100:
            print("⚠️ Out of bounds! Please guess a number between 1 and 100.\n")
            continue
            
        # 3. Evaluate the player's guess
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the correct number: {secret_number}!")
            break
        elif guess < secret_number:
            print("📉 Too low! Try a higher number.\n")
        else:
            print("📈 Too high! Try a lower number.\n")
            
        attempts_left -= 1
        
    # 4. Handle game over scenario
    if attempts_left == 0:
        print("👻 Game Over!")
        print(f"The correct number was: {secret_number}. Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()
