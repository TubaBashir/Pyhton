import math

def get_positive_float(prompt):
    """Ensures the user inputs a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Value must be greater than zero. Please try again.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid numeric value.")

def generate_interest_report():
    print("=== Advanced Financial Interest Calculator ===")
    
    # 1. Gather validated user inputs
    principal = get_positive_float("Enter the initial principal investment ($): ")
    annual_rate = get_positive_float("Enter the annual interest rate (e.g., 5.5 for 5.5%): ")
    years = int(get_positive_float("Enter the investment duration in years: "))
    
    print("\nSelect Interest Type:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    choice = input("Enter choice (1 or 2): ").strip()
    
    # Convert percentage rate to a decimal format
    rate_decimal = annual_rate / 100
    
    print("\n" + "="*65)
    print(f"{'Year':<6}{'Starting Balance':<18}{'Interest Earned':<18}{'Ending Balance':<18}")
    print("="*65)
    
    current_balance = principal
    total_interest_earned = 0
    
    # 2. Simple Interest Logic
    if choice == '1':
        # Simple interest earns a fixed amount every year based entirely on the baseline principal
        yearly_interest = principal * rate_decimal
        for year in range(1, years + 1):
            starting = current_balance
            current_balance += yearly_interest
            total_interest_earned += yearly_interest
            print(f"{year:<6}${starting:<17,.2f}${yearly_interest:<17,.2f}${current_balance:<17,.2f}")
            
    # 3. Compound Interest Logic
    else:
        print("\nSelect Compounding Frequency:")
        print("1. Annually (1x/year)")
        print("2. Monthly (12x/year)")
        print("3. Daily (365x/year)")
        freq_choice = input("Enter frequency (1, 2, or 3): ").strip()
        
        # Determine periodic compound scale
        if freq_choice == '2':
            n = 12
            freq_label = "Monthly"
        elif freq_choice == '3':
            n = 365
            freq_label = "Daily"
        else:
            n = 1
            freq_label = "Annual"
            
        print(f"\n[Running Compound Interest Report - Compounded {freq_label}]")
        print("="*65)
        print(f"{'Year':<6}{'Starting Balance':<18}{'Interest Earned':<18}{'Ending Balance':<18}")
        print("="*65)

        for year in range(1, years + 1):
            starting = current_balance
            # Formula for compound growth over one individual year interval
            # End Balance = P * (1 + r/n)^(n)
            ending = starting * math.pow((1 + rate_decimal / n), n)
            yearly_interest = ending - starting
            total_interest_earned += yearly_interest
            current_balance = ending
            print(f"{year:<6}${starting:<17,.2f}${yearly_interest:<17,.2f}${current_balance:<17,.2f}")

    # 4. Final summary metrics
    print("="*65)
    print(f"Initial Investment : ${principal:,.2f}")
    print(f"Total Interest     : ${total_interest_earned:,.2f}")
    print(f"Final Net Worth    : ${current_balance:,.2f}")
    print("="*65)

if __name__ == "__main__":
    generate_interest_report()
