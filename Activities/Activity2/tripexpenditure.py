class Expense:
    def __init__(self, description, amount, category, paid_by):
        self.description = description
        self.amount = float(amount)
        self.category = category
        self.paid_by = paid_by


class TripBudgetTracker:
    def __init__(self, trip_name, travelers):
        self.trip_name = trip_name
        self.travelers = travelers
        self.expenses = []

    def add_expense(self, description, amount, category, paid_by):
        """Logs a new transaction into the trip profile."""
        if paid_by not in self.travelers:
            print(f"❌ Error: {paid_by} is not registered as a traveler on this trip.")
            return False
            
        expense = Expense(description, amount, category, paid_by)
        self.expenses.append(expense)
        print(f"✅ Logged: '{description}' - ₹/{amount:,.2f} under {category}.")
        return True

    def get_total_spending(self):
        """Calculates aggregate spending across the entire trip."""
        return sum(exp.amount for exp in self.expenses)

    def get_category_breakdown(self):
        """Groups expenses by category for budget analysis."""
        breakdown = {}
        for exp in self.expenses:
            breakdown[exp.category] = breakdown.get(exp.category, 0.0) + exp.amount
        return breakdown

    def calculate_splits(self):
        """
        Calculates how much each person spent and balances sheets.
        Positive value means they are owed money; negative means they owe money.
        """
        total = self.get_total_spending()
        share_per_person = total / len(self.travelers) if self.travelers else 0
        
        # Track raw amounts paid by each individual
        balances = {person: 0.0 for person in self.travelers}
        for exp in self.expenses:
            balances[exp.paid_by] += exp.amount
            
        # Subtract the fair share to see who is over/under paid
        settlements = {person: paid - share_per_person for person, paid in balances.items()}
        return share_per_person, settlements

    def display_summary(self):
        """Prints a comprehensive scannable receipt overview."""
        total = self.get_total_spending()
        per_person, settlements = self.calculate_splits()
        
        print("\n" + "="*40)
        print(f"✈️  TRIP SUMMARY: {self.trip_name.upper()}")
        print("="*40)
        print(f"💰 Total Expenditure : ₹/{total:,.2f}")
        print(f"👥 Group Size        : {len(self.travelers)} people")
        print(f"📉 Cost Per Person   : ₹/{per_person:,.2f}")
        
        print("\n🗂️  Spending by Category:")
        for cat, amt in self.get_category_breakdown().items():
            percentage = (amt / total) * 100 if total > 0 else 0
            print(f" 🔹 {cat:<12}: ₹/{amt:10,.2f} ({percentage:5.1f}%)")
            
        print("\n⚖️  Final Balance Sheets:")
        for person, balance in settlements.items():
            if balance > 0:
                print(f" 🟢 {person:<10}: Owed ₹/{balance:,.2f}")
            elif balance < 0:
                print(f" 🔴 {person:<10}: Owes ₹/{abs(balance):,.2f}")
            else:
                print(f" ⚪ {person:<10}: Completely Settled")
        print("="*40)


# --- Simulation Run ---
if __name__ == "__main__":
    # 1. Initialize a trip with 3 friends
    my_trip = TripBudgetTracker("Goa Getaway", ["Arjun", "Priya", "Rohan"])
    
    # 2. Populate transaction history
    my_trip.add_expense("Villa Booking", 15000, "Lodging", "Arjun")
    my_trip.add_expense("Beach Dinner", 4500, "Food", "Priya")
    my_trip.add_expense("Scooter Rentals", 2400, "Transport", "Rohan")
    my_trip.add_expense("Fuel refill", 600, "Transport", "Rohan")
    my_trip.add_expense("Water Sports", 6000, "Activities", "Arjun")

    # 3. Print out structural balance reports
    my_trip.display_summary()
