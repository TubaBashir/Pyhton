import random
import time

# =========================================================
# CORE GAMEPLAY MATRIX ENGINE
# =========================================================


def determine_winner(player_move, computer_move):
    """Evaluates the win/loss state based on Rock-Paper-Scissors rules."""
    if player_move == computer_move:
        return "tie", "It's a draw! Both chose the same move."

    # Mapping rules: Key beats Value
    win_matrix = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if win_matrix[player_move] == computer_move:
        return "player", f"🏆 You win! {player_move.title()} beats {computer_move.title()}."
    else:
        return (
            "computer",
            f"💻 Computer wins! {computer_move.title()} beats {player_move.title()}.",
        )


# =========================================================
# GAME RUNTIME EXECUTION FRAMEWORK
# =========================================================


def run_game_loop():
    """Manages full application states, scorekeeping, and UI reporting."""
    valid_moves = ["rock", "paper", "scissors"]

    # Score Metrics
    player_score = 0
    computer_score = 0
    ties = 0
    round_number = 1

    print("=========================================================")
    print("           WELCOME TO ROCK, PAPER, SCISSORS              ")
    print("=========================================================")
    print("Rules: First to input an item wins a round.")
    print("Type 'quit' or 'exit' at any prompt to finish playing.\n")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_input = (
            input("Enter your move (Rock, Paper, or Scissors): ")
            .strip()
            .lower()
        )

        # Graceful Session Termination Check
        if user_input in ["quit", "exit"]:
            break

        # Input Integrity Check
        if user_input not in valid_moves:
            print(
                "❌ Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'."
            )
            continue

        # Generate Computer Move
        print("Computer is thinking...")
        time.sleep(0.6)  # Subtle pacing layout delay
        computer_move = random.choice(valid_moves)
        print(f"Computer selected: {computer_move.title()}")

        # Process Matrix State Output Rules
        outcome, round_message = determine_winner(user_input, computer_move)
        print(round_message)

        # Metrics Tracking Adjustments
        if outcome == "player":
            player_score += 1
        elif outcome == "computer":
            computer_score += 1
        else:
            ties += 1

        # Current Scoreboard Snapshot Report
        print(
            f" scoreboard Score: [ You: {player_score} | Computer: {computer_score} | Draws: {ties} ]"
        )
        round_number += 1

    # =========================================================
    # POST-GAME SCOREBOARD WRAP-UP SUMMARY
    # =========================================================
    print("\n=========================================================")
    print("                  FINAL MATCH RESULTS                    ")
    print("=========================================================")
    print(f"Total Rounds Run:   {round_number - 1}")
    print(f"Your Final Wins:    {player_score}")
    print(f"Computer Wins:      {computer_score}")
    print(f"Total Drawn Ties:   {ties}")
    print("---------------------------------------------------------")

    if player_score > computer_score:
        print("👑 GRAND CHAMPION RESULT: YOU BEAT THE MACHINE!")
    elif computer_score > player_score:
        print("🤖 GRAND CHAMPION RESULT: THE COMPUTER WINS THIS MATCH.")
    else:
        print("🤝 GRAND CHAMPION RESULT: THE MATCH ENDS IN A PERFECT DEADLOCK.")
    print("=========================================================\n")
    print("Thank you for playing! Goodbye.")


if __name__ == "__main__":
    run_game_loop()
