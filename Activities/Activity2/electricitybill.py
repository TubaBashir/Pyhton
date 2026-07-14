# Input total units consumed
units = float(input("Enter the total units consumed: "))

# Calculate bill based on tiered pricing slabs
if units <= 100:
    bill = units * 1.50      # $1.50 per unit for first 100 units
elif units <= 300:
    bill = (100 * 1.50) + ((units - 100) * 2.50)  # $2.50 per unit for next 200 units
else:
    bill = (100 * 1.50) + (200 * 2.50) + ((units - 300) * 4.00) # $4.00 per unit above 300 units

# Add a flat service charge/tax
fixed_charge = 25.00
total_bill = bill + fixed_charge

print(f"\nEnergy Charges: ${bill:.2f}")
print(f"Fixed Service Charge: ${fixed_charge:.2f}")
print(f"Total Amount Due: ${total_bill:.2f}")
