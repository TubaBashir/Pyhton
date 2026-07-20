import random

def play_game():
    # 1. Define game choices and initialize scores
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    print("🪨 📄 ✂️ Welcome to Rock, Paper, Scissors!")
    print("Rules: First to win or type 'exit' to quit.\n")
    
    while True:
        # Display scoreboard
        print(f"📊 Score -> You: {user_score} | Computer: {computer_score}")
        
        # 2. Get and validate user input
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        
        if user_choice == 'exit':
            print("\n👋 Thanks for playing! Final Summary:")
            print(f"🏆 You won {user_score} round(s) | Computer won {computer_score} round(s).")
            break
            
        if user_choice not in choices:
            print("❌ Invalid choice! Please type Rock, Paper, or Scissors.\n")
            continue
            
        # 3. Generate computer choice
        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")
        
        # 4. Determine the winner of the round
        if user_choice == computer_choice:
            print("🤝 It's a tie!\n")
            
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!\n")
            user_score += 1
            
        else:
            print("💥 Computer wins this round!\n")
            computer_score += 1

if __name__ == "__main__":
    play_game()
