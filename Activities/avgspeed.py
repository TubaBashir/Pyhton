# Input total distance and total time taken
distance = float(input("Enter total distance (e.g., in km or miles): "))
time = float(input("Enter total time taken (e.g., in hours): "))

# Ensure we do not divide by zero
if time == 0:
    print("Error: Time cannot be zero.")
else:
    # Calculate average speed (Distance divided by Time)
    avg_speed = distance / time
    print(f"The average speed is: {avg_speed:.2f} per hour")
