# Base price of the vehicle
base_price = 25000
total_cost = base_price

print("--- Welcome to the Ride Customiser ---")
print(f"Base Vehicle Price: ${base_price:,}\n")

# 1. Choose Paint Job
print("Select Paint option:")
print("1. Standard White ($0)\n2. Metallic Obsidian ($500)\n3. Matte Satin Gold ($1,200)")
paint_choice = input("Enter choice (1-3): ")
if paint_choice == "2":
    total_cost += 500
elif paint_choice == "3":
    total_cost += 1200

# 2. Choose Wheel Style
print("\nSelect Wheel option:")
print("1. 17\" Stock Alloys ($0)\n2. 19\" Sport Black Rims ($850)\n3. 21\" Forged Performance ($1,800)")
wheel_choice = input("Enter choice (1-3): ")
if wheel_choice == "2":
    total_cost += 850
elif wheel_choice == "3":
    total_cost += 1800

# Summary
print("\n" + "="*30)
print(f"CUSTOM RIDE SUMMARY")
print(f"Total Configured Cost: ${total_cost:,}")
print("="*30)
