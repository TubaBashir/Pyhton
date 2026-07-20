def convert_days(total_days):
    # Approximating 1 month = 30 days and 1 year = 365 days
    years = total_days // 365
    remaining_days = total_days % 365
    
    months = remaining_days // 30
    days = remaining_days % 30
    
    return years, months, days

# Example usage
input_days = 465
years, months, days = convert_days(input_days)

print(f"{input_days} days is equal to {years} years, {months} months, and {days} days.")
