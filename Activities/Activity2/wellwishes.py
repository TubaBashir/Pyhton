import random
from datetime import datetime

class WellWishesGenerator:
    def __init__(self):
        # A dictionary pooling different warm messages based on the event
        self.wishes_database = {
            "birthday": [
                "May this year bring you endless joy, success, and beautiful memories!",
                "Wishing you a fantastic day ahead filled with love, laughter, and lots of cake!",
                "Cheers to another incredible year of life! May all your dreams turn into reality."
            ],
            "get_well": [
                "Sending you healing thoughts and a huge hug. Get well soon!",
                "Take all the time you need to rest and recover. Wishing you a speedy return to full health!",
                "Thinking of you during this time. Hoping you feel much better day by day."
            ],
            "success": [
                "Hard work always pays off! So incredibly proud of your fantastic achievement.",
                "This is just the beginning of many more milestones. Congratulations on your well-deserved success!",
                "Wishing you the very best as you step into this exciting new chapter of your journey!"
            ],
            "general": [
                "Just a little reminder that you are appreciated. Have a truly wonderful day ahead!",
                "Sending positive vibes your way to brighten up your week!",
                "May your day be peaceful, productive, and filled with reasons to smile."
            ]
        }

    def _get_time_of_day_greeting(self):
        """Returns Morning, Afternoon, or Evening based on system time."""
        current_hour = datetime.now().hour
        if current_hour < 12:
            return "Good morning"
        elif current_hour < 17:
            return "Good afternoon"
        else:
            return "Good evening"

    def generate_card(self, recipient_name, occasion="general"):
        """Compiles and prints a nicely framed well-wishes card."""
        # Fallback to general if the input occasion isn't recognized
        category = occasion.lower() if occasion.lower() in self.wishes_database else "general"
        
        # Pick a random warm message from the chosen category
        message = random.choice(self.wishes_database[category])
        greeting = self._get_time_of_day_greeting()
        
        # Constructing the visual text card
        card_lines = [
            "✨" * 25,
            f"💌  {greeting}, {recipient_name}!  💌",
            "",
            f"👉 {message}",
            "",
            "✨" * 25
        ]
        
        # Print out the card block
        print("\n".join(card_lines))


# --- Demonstration Run ---
if __name__ == "__main__":
    generator = WellWishesGenerator()
    
    # Example 1: Birthday wish
    generator.generate_card(recipient_name="Alice", occasion="birthday")
    
    # Example 2: Recovery wish
    generator.generate_card(recipient_name="Bob", occasion="get_well")
