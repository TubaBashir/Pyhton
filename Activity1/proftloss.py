# Input cost price and selling price
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

# Calculate difference
diff = selling_price - cost_price

# Determine profit or loss
if diff > 0:
    percentage = (diff / cost_price) * 100
    print(f"Profit: ${diff:.2f} ({percentage:.2f}%)")
elif diff < 0:
    percentage = (abs(diff) / cost_price) * 100
    print(f"Loss: ${abs(diff):.2f} ({percentage:.2f}%)")
else:
    print("No Profit No Loss")
