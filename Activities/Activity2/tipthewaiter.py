def calculate_split_bill(bill_amount, tip_percentage, people_count):
    # 1. Calculate tip amount and total cost
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount
    
    # 2. Divide total cost by number of people
    amount_per_person = total_bill / people_count
    
    return {
        "tip_amount": tip_amount,
        "total_bill": total_bill,
        "per_person": amount_per_person
    }

def main():
    print("🍽️  Welcome to the Restaurant Tip & Split Calculator")
    
    try:
        # Get raw transaction details from user
        bill = float(input("Enter the total bill amount (₹/$): "))
        tip_percent = float(input("Enter tip percentage (e.g., 10, 15, 20): "))
        people = int(input("How many people are splitting the bill? "))
        
        # Simple input verification
        if bill <= 0 or tip_percent < 0 or people <= 0:
            print("❌ Input values must be greater than zero.")
            return
            
        results = calculate_split_bill(bill, tip_percent, people)
        
        # Display the formatted breakdown
        print("\n📊 Receipt Summary:")
        print(f"🔹 Subtotal        : {bill:.2f}")
        print(f"🔹 Tip Amount     : {results['tip_amount']:.2f} ({tip_percent}%)")
        print(f"🔹 Total Bill     : {results['total_bill']:.2f}")
        print(f"🔹 Per Person Owes: {results['per_person']:.2f}")
        
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
