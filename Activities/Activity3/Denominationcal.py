def calculate_denominations(amount):
    # List of available currency denominations in descending order
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}

    for denom in denominations:
        if amount >= denom:
            count = amount // denom  # Number of notes/coins
            result[denom] = count
            amount = amount % denom  # Remaining amount

    return result


# --- Big Example ---
# Total cash amount to break down
large_amount = 18763

breakdown = calculate_denominations(large_amount)

print(f"Denomination breakdown for ₹{large_amount}:\n")
total_notes = 0
for denom, count in breakdown.items():
    print(f"₹{denom: <4} x {count: <5} = ₹{denom * count}")
    total_notes += count

print("-" * 35)
print(f"Total Notes/Coins Used: {total_notes}")
